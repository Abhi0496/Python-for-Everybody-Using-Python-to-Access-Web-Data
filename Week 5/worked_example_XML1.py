import xml.etree.ElementTree as ET

data = '''
<stuff>
    <users>
        <user x = "2">
            <id> 001 </id>
            <name> Chuck </name>
        </user>
        <user x = "7">
            <id> 009 </id>
            <name> Abhi </name>
        </user>
    </users>
</stuff>
        '''
# Here users tag is having a list of user as a children

stuff = ET.fromstring(data)
lst = stuff.findall('users/user')  # Here we are asking to findall 'user' tags which are child of 'users'
# It will return a list

print("User count:", len(lst))  # Finding how many user tag do we have

for item in lst:
    print("Name:", item.find('name').text)
    print("Id:", item.find('id').text)
    print("Attribute:", item.get('x'))
