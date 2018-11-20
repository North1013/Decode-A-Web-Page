#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def request(url):
    """Download the html of website"""
    r = requests.get(url)
    return r.text
    #print(r.text)

def parsing(r_html, output_file):
    """Parse the html to get articles"""
    f = open(output_file, 'w+')
    soup = BeautifulSoup(r_html, features='lxml')
    title = soup.find_all('h2', attrs={'class': 'css-5z5voo esl82me2'})
    for titles in title:
        clean_titles = titles.text + "\n"
        f.write(clean_titles)
    f.close()

def main(url, output_file):
    request(url)
    parsing(request(url), output_file)

# BASE_URL = input("Input BASE_URL:\n")
BASE_URL = "https://www.nytimes.com/"
# OUTPUT_FILE = input("Choose filename to save to:\n")
OUTPUT_FILE = "test.xml"
main(BASE_URL, OUTPUT_FILE)
