from jwscraper import *

START_TEST_STRING = 'Starting test n. {}'
INVALID_URL='not_valid'
EMPTY_URL='https://www.python.org/'

def invalid_url_test():
    print("Testing on invalid url")
    return scrape_video(INVALID_URL)

def empty_url_test():
    print("Testing on an empty url")
    return scrape_video(EMPTY_URL)

def start_tests():
    for i, elem in enumerate(tests):
        print('------------------------')
        print(START_TEST_STRING.format(i))
        try:
            print("The function returned: "+elem())
        except Exception as e:
            print(e)
            continue

tests = [invalid_url_test, empty_url_test]

if __name__ == '__main__':
    start_tests()