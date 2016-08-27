import urllib2
import xml.etree.ElementTree as ET
def parse_xml(url):
    counts=[]
    page=urllib2.urlopen(url)
    tree= ET.parse(page)

    comments = tree.findall('comments/comment')

    for comment in comments:
        counts.append(int(comment.find('count').text))
    return sum(counts)
data = raw_input("Please enter url: ")
print parse_xml(data)
