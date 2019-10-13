def fixtureHTTPPost(id):
    myURL = 'http://localhost:9920'
    myPath = '/users/insert/'+str(id)
    myBody = {'id_city': 1111, 'user_name': 'Sara'}
    myHeader = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    codeSuccessful = 200
    return (myURL, myPath, myBody, myHeader, codeSuccessful)

def fixtureHTTPGet(id):
    myURL = 'http://localhost:9920'
    myPath = '/users/insert/'+str(id)
    codeSuccessful = 200
    return (myURL, myPath, codeSuccessful)

def fixtureHTTPPostUserInsert(id):
    myURL = 'http://localhost:9920'
    myPath = '/users/insert/'+str(id)
    myBody = {'id_city': 1111, 'user_name': 'Sara'}
    myHeader = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = 'insert/' + str(id) + '/userInsert'
    return (myURL, myPath, myBody, myHeader, response)

def fixtureHTTPPostUserUpdate(id):
    myURL = 'http://localhost:9920'
    myPath = '/users/update/'+str(id)
    myBody = {'id_city': 1111, 'user_name': 'Sara'}
    myHeader = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    answere = 'update/' + str(id) + '/userUpdate'
    return (myURL, myPath, myBody, myHeader, answere)
