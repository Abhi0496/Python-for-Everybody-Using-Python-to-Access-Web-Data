import json

data = '''{
  "name" : "Abhi",
  "phone" : {
    "type" : "intl",
    "number" : "+91 902 835 7656"
   },
   "email" : {
     "hide" : "yes"
   }
}'''   # Here Json looks a lot like python dictionary which is key: value pair

stuff = json.loads(data)
# loadstring will take data as input and will return a structured object
# Here it will return a dictionary

print("Name:", stuff['name'])
print("Phone:", stuff['phone']['number'])
print("Attribute:", stuff['email']['hide'])