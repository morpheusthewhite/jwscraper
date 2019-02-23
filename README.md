# jwscraper

A simple python library for scraping video url from JW players. Bypasses CloudFlare protection.

## Installation

```bash
sudo python3 setup.py install
```
You also need to install Mozilla Firefox and its [driver](https://github.com/mozilla/geckodriver/releases)

## Usage

Just

```python
from jwscraper import scrape_video, scrape_save_video
scrape_video(url, bypass_cloudflare=True)
scrape_save_video(url, filename=None, bypass_cloudflare=True)
```

The first function will return the url containing the video in the page whose url is passed;
The second one will save the video in the page as filename if it is None, otherwise the name will be automatically chosen.
