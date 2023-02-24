import json
#1
names = "john peter brian Morgan Adam Maria bart"
ans = names.title()
print (ans)

#4

import re

name = 'CamelCaseName'
name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
print( ["FirstItem", "FriendsList", "MyTuple"] )