# jwscraper
[![codacy coverage](https://img.shields.io/codacy/coverage/16029fd078e1491d98db2272cdc1d9b0.svg)]()
[![codacy code quality](https://img.shields.io/codacy/grade/16029fd078e1491d98db2272cdc1d9b0.svg)]()
[![license](https://img.shields.io/github/license/morpheusthewhite/jwscraper.svg)](https://github.com/morpheusthewhite/jwscraper/blob/master/LICENSE)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/morpheusthewhite/jwscraper/issues)

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
