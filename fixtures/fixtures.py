def fixturePostUserID(id):
    myURL = "http://localhost:9920/users/update/"+str(id)
    myData = {"user_name": "userNewName", "id_city": 5}
    myHeader = {"Content-type": "application/json", "Accept": "text/plain"}
    codeSuccessful = 200
    return (myURL, myData, myHeader, codeSuccessful)
