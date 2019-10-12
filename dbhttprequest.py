import requests
import json

myURL = "http://localhost:9920/users/update/9"
myBody = {'var11' : 0, 'var22' : 'some string', 'var33' : ['listitem1','listitem2',5]}
myHeader = {"Content-type": "application/json", "Accept": "text/plain"}

req = requests.post(myURL, json=myBody, headers=myHeader)

for i in dir(req):
    print(i)
print('\n', "=======================", '\n')

print("02  req._content_consumed = ", req._content_consumed)   #
print("11  req.headers = ", req.headers)            #
print("25  req.status_code = ", req.status_code)        #
print("26  req.text = ", req.text)               #
print("07  req.content = ", req.content)             #
# print("27", req.json())             #
print("28  req.url = ", req.url)             #


body = req.text.split("?")[0]
print(body)

json_str = json.dumps(body)
json_strMy = json.dumps(myBody)
print(json_strMy)
print()
print(eval(body))


# print(json_str)

path = req.text.split("?")[1]
print(path)

















