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
#    for story_heading in soup.find_all(class_="story-heading"):
#        if story_heading.a:
#            print(story_heading.a)
#        else:
#            print(story_heading)
    #titles = soup.find_all(class_="story-heading")
    title = soup.find_all('h2', attrs={'class': 'css-8uvv5f esl82me2'})
    for titles in title:
        print(titles)
        # title_stripped = titles.replace("h", "")
        # print(title_stripped)

def main(url):
    #request(url)
    parsing(request(url))

BASE_URL = input("Input BASE_URL:\n")
main(BASE_URL)
