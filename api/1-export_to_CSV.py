#!/usr/bin/python3
"""script that get data of a api"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    uid = argv[1]
    todos = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                         .format(uid))
    usr_inf = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                           .format(uid))

    task_completed = 0
    task_total = 0
    user_name = usr_inf.json()["name"]

    for task in todos.json():
        if task["completed"] is True:
            task_completed += 1
        task_total += 1

    task_compl_list = []

    for task in todos.json():
        csvcolums = [uid, user_name, task["completed"], task["title"]]
        task_compl_list.append(csvcolums)

    csvheaders = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    with open("{}.csv".format(uid), 'w') as f:
        CsvWri = csv.writer(f)
        CsvWri.writerow(csvheaders)
        CsvWri.writerows(task_compl_list)
