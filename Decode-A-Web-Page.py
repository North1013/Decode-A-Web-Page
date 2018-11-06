#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def request(url):
    """Download the html of website"""
    r = requests.get(url)
    echo (r.text)

def parsing(r_html):
    """Parse the html to get articles"""
    soup = BeautifulSoup(r_html)


def main(url):
    parsing(request(url))

url = input("Input URL")
main(url)
