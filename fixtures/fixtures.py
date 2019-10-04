from dumps import dumps as dmp

def fixturePostUserID():
    # listPartShuffleReady = [3, 0, 2, 7, 6]
    # listPartShuffleEtalon = [3, 0, 2, 7, 6]
    # base = 5
    # sep = 3
    # low = 0
    # high = len(listPartShuffleReady) - 1
    myURL = “localhost:9920”
    myData = {"user_name": "userNewName", "id_city": 5}
    myHeader = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    codeSuccessful = 200

    return (listPartShuffleReady, listPartShuffleEtalon, base, sep, low, high)

def fixtureEtalon():
    listEtalon = dmp.dumpEtalon()
    return (listEtalon, listEtalon)


