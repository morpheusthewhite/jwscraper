# jwscraper

A simple python library for scraping video url from JW players. Bypasses CloudFlare protection.

#### Installation

```bash
sudo python3 setup.py install
```
You also need to install Mozilla Firefox and its [driver](https://github.com/mozilla/geckodriver/releases)

### Usage

Just

```python
from jwscraper import scrape_video
scrape_video(url, bypass_cloudflare=True)
```

and pass the url of the page containing the video. It will return the url of the video (then you can download it with `requests`, `urllib3` or any other tool/library).
