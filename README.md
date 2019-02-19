# jwscraper

A python library for scraping video url from JW players. Bypasses CloudFlare protection.

### Requirements
To install all python dependencies just run
```bash
pip3 install selenium cfscrape bs4
```

You also need to install Mozilla Firefox and its [driver](https://github.com/mozilla/geckodriver/releases)

### Usage

Just call

```python
scrape_video(url, bypass_cloudflare=True)
```

and pass the url of the page containing the video. It will return the url of the video (then you can download it with `requests`, `urllib3` or any other tool/library).
