print(requests.post('http://127.0.0.1:8000/api/records/', data={"name":"test2", "number": "912345678"}).text) - add new
print(requests.get('http://127.0.0.1:8000/api/record/').text) - get all
print(requests.get('http://127.0.0.1:8000/api/record/', params={"name":"test1"}).text) - get all with such name
print(requests.delete('http://127.0.0.1:8000/api/records/<NAME>/').text) - delete <NAME> ()
