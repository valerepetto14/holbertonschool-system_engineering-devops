#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python script to export
data in the CSV format.s"""
import json
import requests
import sys

if __name__ == '__main__':
    try:
        name_file = 'todo_all_employees.json'
        url = 'https://jsonplaceholder.typicode.com/users'
        url1 = 'https://jsonplaceholder.typicode.com/todos'
        """hago las request"""
        users = requests.get(url)
        tareas = requests.get(url1)

        """defino variables a usar"""

        with open(name_file, 'w', encoding='utf-8') as f:
            for user in users.json():
                lista_task = []
                dic_final = {}
                for tarea in tareas.json():
                    if tarea['userId'] == user['id']:
                        """reseteo el dic para volver a llenarlo"""
                        dic_tareas = {}
                        """lleno el dic con sus valores"""
                        dic_tareas['USER_ID'] = user['id']
                        dic_tareas['task'] = tarea['title']
                        dic_tareas['completed'] = tarea['completed']
                        """agrego el dic a la lista final"""
                        lista_task.append(dic_tareas)
                    """agrego la lista al value de la key id"""
                    dic_final[user['id']] = lista_task
                    """serealizo el diccionario y lo escribo en el documento"""
                    f.write(json.dumps(dic_final))
    except Exception as e:
        print(e)
