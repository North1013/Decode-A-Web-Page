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
    titles = soup.find('h2', attrs={'class': 'esl82me2'})
    #title = soup.find('span', 'balancedHeadline')
    for title in titles:
        print(title)

def main(url):
    #request(url)
    parsing(request(url))

BASE_URL = input("Input BASE_URL:\n")
main(BASE_URL)