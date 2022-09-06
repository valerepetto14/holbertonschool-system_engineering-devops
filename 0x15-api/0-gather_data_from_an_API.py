#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""
import json
import requests
import sys

if __name__ == '__main__':
    id = sys.argv[1]
    ul = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    ul1 = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id)
    data = requests.get(ul)
    todos = requests.get(ul1)

    name = data.json()['name']
    titles = []
    done_tasks = 0
    all_tasks = 0
    for i in todos.json():
        all_tasks += 1
        if i.get('completed') is True:
            done_tasks += 1
            titles.append(i['title'])
    print("Employee {} is done with tasks({}/{}):".format(name, done_tasks,
          all_tasks))
    for task in titles:
        print("\t {}".format(task))
