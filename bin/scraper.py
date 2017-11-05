#!/usr/bin/python2.7
'''
This script scrapes twitter moments and prints
each url and title
'''

import requests
import sys

from bs4 import BeautifulSoup


def main():
    for link in twitter_handler():
        print link


def twitter_handler(url='http://twitter.com/i/moments'):
    body = get_contents(url)
    for div in body.find_all('div'):
        div_class = div.get('class')
        if not div_class or not 'MomentCapsuleSummary-details' in div_class:
            continue
        yield _get_twitter_urls(div)


def _get_twitter_urls(div):
    for link in div.find_all('a'):
        url = link.get('href')
        title = link.get('title')
        title = title.encode('ascii', 'xmlcharrefreplace')
        return '{}|{}'.format(url, title)


def get_contents(url):
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    return soup.body


if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print err
