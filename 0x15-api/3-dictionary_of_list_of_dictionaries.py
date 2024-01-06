#!/usr/bin/python3
"""
    Script to gather TODO's of an employee using employee ID
"""
import json
from requests import get
from sys import argv

DATA_ENDPOINT = "https://jsonplaceholder.typicode.com"
TASK_TITLES = []
TASKS = {}


def get_users():
    """
        gets the details of a user
    """
    global TASK_TITLES
    response = get(url=f"{DATA_ENDPOINT}/users")
    response.raise_for_status()
    data = response.json()
    for user in data:
        id = user['id']
        username = user['username']
        TASKS[f"{id}"] =  get_todos(id, username)
        TASK_TITLES = []


def get_todos(id, username):
    """
        queries the endpoint for user's todo list
    """
    response = get(url=f"{DATA_ENDPOINT}/users/{id}/todos")
    data = response.json()
    for todo in data:
        TASK_TITLES.append({"username": username,
                            "task": todo['title'],
                            "completed": todo['completed']
                            })
    return TASK_TITLES
        


if __name__ == "__main__":
    get_users()
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(TASKS, jsonfile)
