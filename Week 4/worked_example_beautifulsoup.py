# http://www.dr-chuck.com/ and go to view page source
# https://www.si.umich.edu/

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re


# Import SSL certificate error
# if some site have some certificates which are not in pythons official list
# below codes helps to retrieve those pages also
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("Enter: ")  # Asking the user for url
html = urllib.request.urlopen(url, context= ctx).read()
# read() will read complete blog and will return one complete document of string which will be in UTF8
# BeautifulSoup knows how to read UTF8 or unicode strings

soup = BeautifulSoup(html, 'html.parser')
# BS takes complete html parse it using html parser and we get a object which is assigned to soup here
# Internal structure of the soup object will be like tree

# Retrieve all the anchor tags <a ......... </a>
tags = soup('a')  # This is return a list of all the tags


# Below for loop as not as per the course. I have modified little bit
# I have used regular expressions so that it will print only the http links
for tag in tags:
    x = tag.get('href', None)
    if re.match('^http.+', x):
        print(x)