#!/bin/python
#Importing modules
from lxml import html
import requests
import itertools

response = requests.get('http://packtpub.com/')
tree = html.fromstring(response.content)
#Create the list of Books:
books = tree.xpath('//div[@class="book-block-title"]/text()')


print books

