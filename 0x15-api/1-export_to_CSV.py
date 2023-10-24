#!/usr/bin/python3
""" Extend a module to export data in the CSV format."""
import csv
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    # Employee's id
    user_id = int(sys.argv[1])
    user_endpoint = "{}/users/{}".format(url, user_id)

    # Empmpolyee's username
    username = requests.get(user_endpoint).json().get("username")
    tasks_endpoint = "{}/todos".format(url)

    # Employees todo
    tasks = requests.get(tasks_endpoint).json()
    user_tasks = [[user_id, username,
                   task.get("completed"),
                   task.get("title")]
                  for task in tasks if user_id == task.get("userId")]

    # Open a file for writing CSV data
    with open('{}.csv'.format(user_id), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        # Write each row of data to the CSV file
        for row in user_tasks:
            writer.writerow(row)
