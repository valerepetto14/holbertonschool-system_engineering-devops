#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python script to export
data in the CSV format.s"""
import json
import requests
import sys

if __name__ == '__main__':
    try:
        id = sys.argv[1]
        name_file = '{}.json'.format(id)
        ul = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
        ul1 = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(id)
        """hago las request"""
        user = requests.get(ul)
        tareas = requests.get(ul1)

        """defino variables a usar"""
        username = user.json()['username']
        lista_task = []
        dic_final = {}
    
        with open(name_file, 'w', encoding='utf-8') as f:
            for tarea in tareas.json():
                """reseteo el dic para volver a llenarlo"""
                dic_tareas = {}
                """lleno el dic con sus valores"""
                dic_tareas['task'] = tarea['title']
                dic_tareas['completed'] = tarea['completed']
                dic_tareas['username'] = username
                """agrego el dic a la lista final"""
                lista_task.append(dic_tareas)
            """agrego la lista al value de la key id"""
            dic_final[id] = lista_task
            """serealizo el diccionario y lo escribo en el documento .json"""
            f.write(json.dumps(dic_final))
    except Exception as e:
        print(e)
