import re
allNumbers = list()
handle = open('regex_sum_268651.txt')
for line in handle:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        allNumbers.append(int(number))
print sum(allNumbers)
