 - add new
`print(requests.post('http://phonebookexample.herokuapp.com/api/records/', data={"name":"test2", "number": "912345678"}).text)`
 - get all
`print(requests.get('http://phonebookexample.herokuapp.com/api/record/').text)`
 - get all with such name
`print(requests.get('http://phonebookexample.herokuapp.com/api/record/', params={"name":"test1"}).text)`
 - delete <NAME>
`print(requests.delete('http://phonebookexample.herokuapp.com/api/records/<NAME>/').text)`

	Add branch

