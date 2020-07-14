import re

hand = open('regex_sum_99126.txt')
c = 0

for line in hand:
    line = line.strip()

    # Here [0-9] means single digit/number "+" mean one or more that one time
    stuff = re.findall('[0-9]+',line)

    # Stuff will return list of strings, here I am converting them into integers
    stuff = [int(i) for i in stuff]
    c = c + sum(stuff)

print(c)