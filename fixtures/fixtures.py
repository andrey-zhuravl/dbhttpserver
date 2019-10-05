def fixturePostUserID():
    myURL = "localhost:9920"
    myData = {"user_name": "userNewName", "id_city": 5}
    myHeader = {"Content-type": "application/json", "Accept": "text/plain"}
    codeSuccessful = 200
    return (myURL, myData, myHeader, codeSuccessful)
