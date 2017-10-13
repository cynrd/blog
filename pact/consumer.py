import requests
import sys

def user(gateway, user_name):
    """Fetch a user object by user_name from the server."""
    uri = gateway + '/users/' + user_name
    response = requests.get(uri)
    return response.json()

if __name__ == '__main__':
	print(user('http://localhost', sys.argv[1]))
