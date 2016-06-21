from bs4 import BeautifulSoup
import requests
import requests.exceptions
import urlparse	
from collections import deque
import re

# a queue of urls to be crawled
urls = deque(['https://www.packtpub.com/'])

# a set of urls that we have already crawled
scraped_urls = set()

# a set of crawled emails
emails = set()

# Scrape urls one by one queue is empty
while len(urls):

    # move next url from the queue to the set of processed urls
    url = urls.popleft()
    scraped_urls.add(url)

    # extract base url to resolve relative links
    parts = urlparse.urlsplit(url)
    base_url = "{0.scheme}://{0.netloc}".format(parts)
    path = url[:url.rfind('/')+1] if '/' in parts.path else url

    # get url's content
    print("Processing %s" % url)
    try:
        response = requests.get(url)
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        # ignore pages with errors
        continue

    # Search email addresses and add them into the output set
    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
    emails.update(new_emails)

    # create a beutiful soup
    soup = BeautifulSoup(response.text)

    # find and process all the anchors
    for anchor in soup.find_all("a"):
        # extract link url
        link = anchor.attrs["href"] if "href" in anchor.attrs else ''
        # resolve relative links
        if link.startswith('/'):
            link = base_url + link
        elif not link.startswith('http'):
            link = path + link
        # add the new url to the queue
        if not link in urls and not link in scraped_urls:
            urls.append(link)
    print(emails)
