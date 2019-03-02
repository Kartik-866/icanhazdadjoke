import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

print(colored(figlet_format('icanhazdadjoke'), color = 'magenta'))
term = input('What would you like to search for? ')

url = 'https://icanhazdadjoke.com/search'
response = requests.get(url, headers= {'Accept': 'application/json'}, params = {'term': term}).json()

if not response['total_jokes']:
    print(f'Sorry! No jokes found for {term}')
else:
    print(choice(response['results'])['joke'])
