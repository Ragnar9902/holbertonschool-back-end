#!/usr/bin/python3
"""script that get data of a api"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    all_users = requests.get("https://jsonplaceholder.typicode.com/users")
    users_dict = {}

    for user in all_users.json():
        uid = user['id']
        user_name = user["name"]
        todos = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                             .format(uid))
        task_list = []
        
        for task in todos.json():
            task_list.append({"username": user_name,
                              "task": task["title"],
                              "completed": task["completed"]})
        
        users_dict["{}".format(uid)] = task_list

    with open("todo_all_employees.json".format(uid), 'w') as f:
        json.dump(users_dict, f)
