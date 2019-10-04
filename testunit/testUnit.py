import unittest

from fixtures import fixtures as fx
from myQuickSort import myQuickSort as qs
import requests

class myTestQuickSort(unittest.TestCase):

    def test_reuestsToHTTPServer(self):
        (httpURL, jsonData, base, sepEtalon, low, high) = fx.fixturePartShuffleReady()
        (listResult, sepPart) = qs.partition(listOriginal, base, low, high)
        self.assertEqual(listResult, listEtalon)
        self.assertEqual(sepEtalon, sepPart)


        r = requests.post('http://httpbin.org/post', json={"key": "value"})
        r.status_code
        r.json()

        url = "http://localhost:8080"
        data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        requests.post

        # 1. путь
        # 2. тело в формате json
        # 3. заголовки)


if __name__ == '__main__':
    unittest.main()
