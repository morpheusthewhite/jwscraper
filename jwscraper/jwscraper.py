import cfscrape
import bs4
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.common.exceptions import NoSuchElementException
from jwscraper.no_video_available_exception import *


PLAY_BUTTON_CLASS = 'jw-icon jw-icon-display jw-button-color jw-reset'
VIDEO_ELEMENT_CLASS = 'jw-video jw-reset'


def get_unprotected_link(url: str) -> str:
    """
    Returns the link to a page whose only element is the jw player, avoiding any cloudflare protection
    """
    # creates a scraper instance
    scraper = cfscrape.create_scraper()
    # and retrieves the content of the html
    html = scraper.get(url).content

    # parsing content of html
    soup = bs4.BeautifulSoup(html, 'html.parser')
    iframes = soup.find_all('iframe')

    # iterating over iframes looking for the one that resembles a link
    result_url = ''
    for iframe in iframes:
        if 'http' in iframe['src']:
            result_url = iframe['src']
    
    # checking if a valid url has been found
    if result_url == '':
        raise NoVideoAvailableException
    else:
        return result_url


def scrape_video_no_protection(url: str) -> str:
    # opens a driver on the given url
    options = FirefoxOptions();
    options.add_argument("-headless")

    driver = webdriver.Firefox(options=options)  
    driver.get(url)
    
    try:
        # clicks play to start video and load video url in the page
        play_button = driver.find_element_by_xpath("//div[@class = '{}']".format(PLAY_BUTTON_CLASS))
        play_button.click()

        # gets video url from page once is loaded
        video_player_element = driver.find_element_by_xpath("//video[@class = '{}']".format(VIDEO_ELEMENT_CLASS))
        video_url = video_player_element.get_attribute('src')   
    except NoSuchElementException:
        raise NoVideoAvailableException

    # closes driver
    driver.close()

    return video_url


def scrape_video(url: str, bypass_cloudflare: bool=True) ->str:
    if bypass_cloudflare:
        url = get_unprotected_link(url)

    return scrape_video_no_protection(url)
