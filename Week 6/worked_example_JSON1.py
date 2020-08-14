# Here data is list of dictionaries
import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Abhi"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Ken"
  }
]
'''
# In JS its array of objects but in Python its list of dictionaries

stuff = json.loads(data)  # It will parse it and will convert this JSON into Python list in this case
print(len(stuff))

for item in stuff:
    print('ID:', item['id'])
    print('Name:', item['name'])
    print('Attribute:', item['x'])