#!/usr/bin/python3
""" Json representation of Employee's Data """
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    emp_id = int(sys.argv[1])
    user_endpoint = "{}/users/{}".format(url, emp_id)
    username = requests.get(user_endpoint).json().get("username")
    tasks_endpoint = "{}/todos".format(url)
    tasks = requests.get(tasks_endpoint).json()
    user_tasks = {emp_id: [{"task": task.get("title"),
                            "completed": task.get("completed"),
                            "username": username}
                  for task in tasks if task.get("userId") == emp_id]
                  }

    # save in json file
    with open("{}.json".format(emp_id), 'w', encoding="utf-8") as f:
        json.dump(user_tasks, f)
