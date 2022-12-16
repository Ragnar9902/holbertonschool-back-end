#!/usr/bin/python3
"""script that get data of a api"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    users_url = "https://jsonplaceholder.typicode.com/users?id="
    from collections import defaultdict
    users_dict = defaultdict(list)

    for item in todos.json():
        uid = item['id']
        url = users_url + str(item['userId'])
        usr_resp = requests.get(url).json()
        user_name = usr_resp[0]["username"]
        
        all_item = {"username": user_name,
                     "task": item["title"],
                     "completed": item["completed"]}

        users_dict["{}".format(uid)].append(all_item)

    with open("todo_all_employees.json".format(uid), 'w') as f:
        json.dump(users_dict, f)
