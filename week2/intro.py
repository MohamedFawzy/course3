import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print line
    if re.search('^X.*:', line):
        print line
x = 'my 2 favorites number are 19 and 92'
y = re.findall('[0-9]', x)
print y
