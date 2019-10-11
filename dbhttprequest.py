import requests
import json

myURL = "http://localhost:9920/users/update/9"
myData = {'var11' : 0, 'var22' : 'some string', 'var33' : ['listitem1','listitem2',5]}
myHeader = {"Content-type": "application/json", "Accept": "text/plain"}

req = requests.post(myURL, json=myData, headers=myHeader)

for i in dir(req):
    print(i)
print('\n', "=======================", '\n')

print("2", req._content_consumed)   #
print("7", req.content)             #
print("9", req.elapsed)             #
print("11", req.headers)            #
print("23", req.reason)             #
print("24", req.request)            #
print("25", req.status_code)        #
print("26", req.text)               #
print("27", req.json())             #


















