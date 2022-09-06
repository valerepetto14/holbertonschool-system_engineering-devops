#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python script to export
data in the CSV format.s"""
import json
import requests
import sys

if __name__ == '__main__':
    try:
        id = sys.argv[1]
        name_file = '{}.csv'.format(id)
        ul = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
        ul1 = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id)
        data = requests.get(ul)
        todos = requests.get(ul1)
        with open(name_file, 'w', encoding = 'utf-8') as f:
            for tarea in tareas.json():
                userid = tarea.get('userId')
                name = data.json().get('username')
                completed = tarea.get('completed')
                title = tarea.get('title')
                f.write('"{}","{}","{}","{}"\n'.format(userid, name, completed, title))
    except Exception as e:
        print(e)
