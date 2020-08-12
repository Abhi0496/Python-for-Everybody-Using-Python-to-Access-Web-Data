# http://py4e-data.dr-chuck.net/comments_42.xml
# http://py4e-data.dr-chuck.net/comments_724428.xml
# For explanation of code please check other examples of week 5

import urllib.request
import xml.etree.ElementTree as ET

fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_724428.xml').read()

stuff = ET.fromstring(fhand)
lst = stuff.findall('comments/comment')
lst1 = []
for item in lst:
    lst1.append(int(item.find('count').text))
print(sum(lst1))


