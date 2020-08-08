import urllib.request
# urllib is created to make socket/HTTP communications a lot easier

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')  # this is making socket calls underneath it
# Here we are not sending separate get command, not encoding, nothing like socket

counts = dict()
for line in fhand:
    words = line.decode().split()  # line does come back as array of byte instead of strings
    # So we need to do decode() to convert it into string

    for word in words:
        counts[word] = counts.get(word, 0) + 1
        # counting frequency of words

print(counts)

