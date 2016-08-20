import urllib
from bs4 import BeautifulSoup
url = raw_input("Enter - ")
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# retreive  a list of anchor tags
# each tag is like a dictionary of html attributes
tags = soup('a')
for tag in tags:
    print tag.get('href',None)
