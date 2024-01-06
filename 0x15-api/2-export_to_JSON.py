#!/usr/bin/python3
"""
This script gathers TODO's of an employee using their employee ID and exports
the data to a JSON file.

The script makes use of the json and requests modules to interact with a
REST API. It retrieves the username of the employee using their ID and then
queries the API to get the employee's todo list.

The script then creates a JSON file named after the
employee ID and writes the todo list data to it.

Usage: python3 2-export_to_JSON.py [employee_id]
"""
import json
from requests import get
from sys import argv

DATA_ENDPOINT = "https://jsonplaceholder.typicode.com"
EMPLOYEE_ID = argv[1] if argv[1] else ""
TASK_TITLES = []


def get_username():
    """
    Retrieves the username of the employee using their ID.

    Returns:
        str: The username of the employee.
    """
    response = get(url=f"{DATA_ENDPOINT}/users/{EMPLOYEE_ID}")
    data = response.json()
    username = data.get('username')
    return username


def get_todos():
    """
    Queries the API to get the employee's todo list and exports
    it to a JSON file.
    """
    response = get(url=f"{DATA_ENDPOINT}/users/{EMPLOYEE_ID}/todos")
    data = response.json()
    username = get_username()
    for todo in data:
        TASK_TITLES.append({"task": todo.get('title'),
                            "completed": todo.get('completed'),
                            "username": username})
    with open(f"{EMPLOYEE_ID}.json", 'w') as jsonfile:
        json.dump({EMPLOYEE_ID: TASK_TITLES}, jsonfile)


if __name__ == "__main__":
    get_todos()
