def fixtureHTTPPost(id):
    myURL = 'http://localhost:9920'
    myPath = '/users/insert/'+str(id)
    myBody = {'id_city': 1111, 'user_name': 'Sara'}
    myHeader = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    codeSuccessful = 200
    return (myURL, myPath, myBody, myHeader, codeSuccessful)

def fixturePostURL(id):
    myURL = 'http://localhost:9920/users/insert/'+str(id)
    myBody = {'user_name': 'Sara', 'id_city': 1111}
    myHeader = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    codeSuccessful = 200
    return (myURL, myBody, myHeader, codeSuccessful)

def fixturePostPath(id):
    myURL = 'http://localhost:9920/users/insert/'+str(id)
    myBody = {'user_name': 'Sara', 'id_city': 1111}
    myHeader = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    return (myURL, myBody, myHeader)
