'''
API & JSON - Fetching data from an API and parsing JSON data using requests and json modules/libraries.

API - Application Programming Interface
- A set of rules that allows one software application to talk to another software application.
- The API defines the correct way for a developer to write a program that requests services from an operating system (OS) or other application.
The Rules:
- The API tells the developer what requests can be made, what data can be accessed, and how it can be accessed.
- The API is a set of protocols, tools, and definitions that allow different software applications to communicate with each other.

REST API - Representational State Transfer API
- A set of rules that developers follow when they create their API.
CRUD Operations:
- Create, Read, Update, Delete
- REST API is based on these operations.
[Get] - Read
[Post] - Create
[Put] - Update
[Delete] - Delete
'''

# Importing the requests and json modules
import requests
import json

# Fetching data from an API [JSONPLaceholder API]
response = requests.get('https://jsonplaceholder.typicode.com/posts')
if response.status_code == 200:  # Status code 200 indicates a successful response
    data = response.json()  # Parsing the JSON data

    # Displaying the data
    print(data) # Data is a list of Objects (Dictionaries)

    print('\n-----------------------------------\n')

    # Displaying the first element of the data
    print(data[0])

print('\n-----------------------------------\n')

# Creating a JSON object to send to an API
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
} # Dictionary

# Converting the data to JSON format
json_data = json.dumps(data)

# Posting the JSON data to an API
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=json_data)
if response.status_code == 201:  # Status code 201 indicates a successful response
    print(response.json())  # Displaying the response data
else:
    print('Error:', response.status_code) # Displaying the error message

print('\n-----------------------------------\n')

# Updating data using an API
json_data2 = json.dumps({
    'title': 'updated title',
    'body': 'updated body',
    'userId': 1
})
response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=json_data2)
if response.status_code == 200:  # Status code 200 indicates a successful response
    print(response.json())  # Displaying the response data
else:
    print('Error:', response.status_code) # Displaying the error message

# Deleting data using an API
response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
if response.status_code == 200:  # Status code 200 indicates a successful response
    print(response.json())  # Displaying the response data
else:
    print('Error:', response.status_code) # Displaying the error message

'''
JSONPLaceholder API doesn't allow data to be created, updated or deleted,
so the above code will return an error message.
'''
