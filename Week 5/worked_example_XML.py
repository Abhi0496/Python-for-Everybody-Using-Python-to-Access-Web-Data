import xml.etree.ElementTree as ET
# ElementTree is a built in XML parser in Python

# Here we are giving XML input
data = '''
 <person>
    <name> Abhishek </name>
    <phone type= "int"> +91 9028357656 </phone>
    <email hide= "Yes"/>
 </person>
    '''

tree = ET.fromstring(data)  # if there's some syntax mistake in data this line will blow up
# Here ET will form a tree structure using fromstring and taking data from data string
print("Name:", tree.find('name').text)
# Here 'name' is a tag and we can get either text out of tag or an attribute from a tag
# For getting text we use .text and for getting attribute we use .get()

print("Phone:", tree.find('phone').text)
print("Phone Attribute:",tree.find('phone').get('type'))
# For getting an attribute we need to use get() and type in attribute name

print("Email Attribute:",tree.find('email').get('hide'))
