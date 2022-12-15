#!/usr/bin/python3
"""script that get data of a api"""

import requests
from sys import argv
import csv

if __name__ == "__main__":
    uid = argv[1]
    todos = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                         .format(uid))
    usr_inf = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                           .format(uid))

    task_completed = 0
    task_total = 0

    for task in todos.json():
        if task["completed"] is True:
            task_completed += 1
        task_total += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(usr_inf.json()["name"], task_completed, task_total))

    task_compl_list = []

    for task in todos.json():
        if task["completed"] is True:
            print("\t {}".format(task["title"]))
            csvcolums = [usr_inf.json()["id"], usr_inf.json()["name"]
                         , task["completed"], task["title"]]
            task_compl_list.append(csvcolums)

    csvheaders = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    with open("USER_ID.csv", 'w') as f:
        CsvWri = csv.writer(f)
        CsvWri.writerow(csvheaders)
        CsvWri.writerows(task_compl_list)
