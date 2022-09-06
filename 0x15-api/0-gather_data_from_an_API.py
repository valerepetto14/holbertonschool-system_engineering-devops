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

        EMPLOYEE_NAME = data.json()['name']
        TOTAL_NUMBER_OF_TASKS = 0
        NUMBER_OF_DONE_TASKS = 0
        TASK_TITLE = []
        for i in todos.json():
            TOTAL_NUMBER_OF_TASKS += 1
            if i.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(i['title'])
        print('Employee {} is done with tasks({}/{}):'.format(EMPLOYEE_NAME,
              NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
        for tarea in TASK_TITLE:
            print("\t {}".format(tarea))
    except Exception:
        print(Exception)
