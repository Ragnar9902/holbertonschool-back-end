#!/usr/bin/python3
"""script that get data of a api"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    uid = int(argv[1])
    todos = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                         .format(uid))
    usr_inf = requests.get("https://jsonplaceholder.typicode.com/users?id={}"
                           .format(uid))

    task_completed = 0
    task_total = 0
    user_name = usr_inf.json()[0]["username"]

    task_list = []

    for task in todos.json():
        task_list.append({"task": task["title"],
                          "completed": task["completed"],
                          "username": user_name})

    with open("{}.json".format(uid), 'w') as f:
        json.dump({"{}".format(uid): task_list}, f)
