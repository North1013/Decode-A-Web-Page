#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def request(url):
    """Download the html of website"""
    r = requests.get(url)
    return r.text
    #print(r.text)

def parsing(r_html):
    """Parse the html to get articles"""
    soup = BeautifulSoup(r_html, features='lxml')
    title = soup.find('title')
    print(title)


def main(url):
    #request(url)
    parsing(request(url))

URL = input("Input URL:\n")
main(URL)
