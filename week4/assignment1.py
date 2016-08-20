import urllib
from bs4 import BeautifulSoup
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
spans = soup('span')
numbers = []
for span in spans:
    numbers.append(int(span.string))
print sum(numbers)
