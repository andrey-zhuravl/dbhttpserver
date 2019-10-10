def fixturePostStatusCode(id):
    myURL = "http://localhost:9920/users/update/"+str(id)
    myData = {"user_name": "Sara", "id_city": 1111}
    codeSuccessful = 200
    return (myURL, myData, codeSuccessful)

def fixturePostURL(id):
    myURL = "http://localhost:9920/users/update/"+str(id)
    myData = {"user_name": "Sara", "id_city": 1111}
    myHeader = {"Content-type": "application/json", "Accept": "text/plain"}
    codeSuccessful = 200
    return (myURL, myData, myHeader, codeSuccessful)

def fixturePostPath(id):
    myURL = "http://localhost:9920/users/update/"+str(id)
    myData = {"user_name": "Sara", "id_city": 1111}
    myHeader = {"Content-type": "application/json", "Accept": "text/plain"}
    return (myURL, myData, myHeader)
