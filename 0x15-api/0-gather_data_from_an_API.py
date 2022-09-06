#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""
import json
import requests
import sys

if __name__ == '__main__':
    try:
        id = sys.argv[1]
        ul = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
        ul1 = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id)
        data = requests.get(ul)
        todos = requests.get(ul1)

        name = data.json().get('name')
        done = 0
        all = 0
        for i in todos.json():
            all += 1
            if i.get('completed') is True:
                done += 1
        print('Employee {} is done with tasks({}/{}):'.format(name, done, all))
        for i in todos.json():
            if i.get('completed') is True:
                print('\t {}'.format(i.get('title')))
    except Exception:
        print(Exception)
