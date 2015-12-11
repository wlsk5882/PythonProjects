'''
author                    : Jina Lee
original creation date    : Dec. 9, 2015
last modification date    : 

Capstone Project Activity 1


1.) Web scrape the following web site:  pick an alert from:  www.us-cert.gov/ncas/alerts
I suggest using the requests external library to do this web scraping.

2.) Then, print the results to the monitor in a readable format,
- as if you wrote the web-site source code yourself (so it's readable, pretty).
I suggest using BeautifulSoup prettify() to do this.

On window machine, type command "chcp 65001" first to avoid charmap error..
since prettify() didn't work with encoding html texts.
-- http://stackoverflow.com/questions/32382686/unicodeencodeerror-charmap-codec-cant-encode-character-u2010-character-m
-- https://wiki.python.org/moin/PrintFails
 
'''

import requests
from bs4 import BeautifulSoup

# gets a response from web page, www.us-cert.gov/ncas/alerts

url = r'https://www.us-cert.gov/ncas/alerts'
#url=r'http://www.yelp.com/pittsburgh'

r = requests.get(url)
#print(r.headers)

content = r.content

soup = BeautifulSoup(content, 'html.parser')
#print(soup.encode('utf-8'))

#print(soup.prettify())

print(soup.prettify())#.encode('utf-8')
