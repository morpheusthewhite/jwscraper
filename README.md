# jwscraper

A python library for scraping video url from JW players. Bypasses CloudFlare protection.

### Requirements
To install all python dependencies just run
```bash
sudo pip3 install -r requirements.txt
```

You also need to install Mozilla Firefox and its [driver](https://github.com/mozilla/geckodriver/releases)

#### Installation

After installing required packages run

```bash
sudo python3 setup.py install
```

### Usage

Just

```python
from jwscraper import scrape_video
scrape_video(url, bypass_cloudflare=True)
```

and pass the url of the page containing the video. It will return the url of the video (then you can download it with `requests`, `urllib3` or any other tool/library).
