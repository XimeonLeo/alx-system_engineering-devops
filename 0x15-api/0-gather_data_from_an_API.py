#!/usr/bin/python3
""" Returns information about an employee's' TODO list progress.
        Using requests module
        First line:
            Employee EMPLOYEE_NAME is done with tasks
                (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
        Second and N next lines display the title of completed
        tasks: TASK_TITLE
        (with 1 tabulation and 1 space before the TASK_TITLE)
"""
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com"
    empId = int(sys.argv[1])

    # employee's endpoint from the url
    emp_EP = "{}/users/{}".format(url, empId)

    # Getting emp's name from endpoint
    name = requests.get(emp_EP).json().get("name")

    # Getting the task endpoint
    task_EP = "{}/todos".format(url)

    # Getting the json of all tasks
    tasks = requests.get(task_EP).json()

    # Getting all tasks for an employee
    emp_task = [task for task in tasks if task.get("userId") == empId]

    # Getting @ll completed tasks
    taskCmplted = [task for task in emp_task if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(taskCmplted), len(emp_task)))

    for task in taskCmplted:
        print("\t {}".format(task.get("title")))
