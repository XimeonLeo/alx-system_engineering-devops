#!/usr/bin/python3
"""A module that, fetchs users data
        <F5>and stores them in a json file
"""
import json
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    # Get all user ids
    users = requests.get('{}users'.format(url)).json()

    # Create a dictionary to store tasks for all users
    users_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']

        # Get all tasks for this user
        user_todos = requests.get('{}todos?userId={}'
                                  .format(url, user_id)).json()

        # Filter tasks for this user
        tasks = []
        for task in user_todos:
            tasks.append({
                "username": username,
                "task": task.get('title'),
                "completed": task.get('completed')
            })

        # Add tasks for this user to dictionary
        users_tasks[user_id] = tasks

    # Save to json file named todo_all_employees.json
    with open('todo_all_employees.json', 'w', encoding='utf-8') as f:
        json.dump(users_tasks, f)
