import requests
import sys

def star(gateway, star_name):
    """Fetch a star object by star_name from the server."""
    uri = gateway + '/star/' + star_name
    response = requests.get(uri)
    return response.json()

if __name__ == '__main__':
	print(user('http://localhost', sys.argv[1]))
