# import xml.etree.ElementTree as ET
# input = '''
# <stuff>
#     <users>
#         <user x= "2">
#             <id>001</id>
#             <name>Chuck</name>
#         </user>
#         <user x= "7">
#             <id>009</id>
#             <name>Brent</name>
#         </user>
#     </users>
# </stuff>'''
#
# stuff = ET.fromstring(input)
# lst = stuff.findall('users/user')
# print 'User count:', len(lst)
#
# for item in lst:
#     print 'Name', item.find('name').text
#     print 'Attribute', item.get('x')


import json

data = '''[{
    "name" :"Chuck",
    "phone" : {
        "type" :"intl",
        "number" : "+1 734 303 4456"
        },
        "email" : {
            "hide" : "yes"
        }
}]'''

info = json.loads(data)
# print 'Name:', info["name"]
# print 'Hide', info["email"]["hide"]






# input = '''[{ "id" : "001","x" : "2","name" : "Chuck"} ,{ "id" : "009","x" : "7","name" : "Brent"}]'''
#
# info = json.loads(input)
# print info
# print 'User count:', len(info)
#
# for item in info:
#     print 'Name', item['name']
#     print 'Id', item['id']
#     print 'Attribute', item['x']
#
