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
        tareas = requests.get(ul1)
        lista_task = []
        dic = {}
        with open(name_file, 'w', encoding = 'utf-8') as f:
            for tarea in tareas.json():
                lista_task.append(tarea)
            dic[id] = lista_task
            f.write(json.dumps(dic))
    except Exception as e:
        print(e)
