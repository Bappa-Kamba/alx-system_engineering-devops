#!/usr/bin/python3
"""
    Script to gather TODO's of an employee using employee ID

    This script retrieves the TODO's of employees by making API requests
    to a data endpoint.
    It collects the TODO's for each user and stores them in a dictionary,
    where the key is the user ID and the value is a list of dictionaries
    containing task information.

    The script then writes the collected data to a JSON file named
    "todo_all_employees.json".

    Usage:
        python3 3-dictionary_of_list_of_dictionaries.py
"""
import json
from requests import get

DATA_ENDPOINT = "https://jsonplaceholder.typicode.com"
TASK_TITLES = []
TASKS = {}


def get_users():
    """
    Retrieves the details of all users and their TODO's.

    Returns:
        None
    """
    global TASK_TITLES
    response = get(url=f"{DATA_ENDPOINT}/users")
    response.raise_for_status()
    data = response.json()
    for user in data:
        id = user['id']
        username = user['username']
        TASKS[f"{id}"] = get_todos(id, username)
        TASK_TITLES = []


def get_todos(id, username):
    """
    Queries the endpoint for a user's todo list and returns a list of
    dictionaries containing task information.

    Args:
        id (int): The user's ID.
        username (str): The username of the user.

    Returns:
        list: A list of dictionaries containing task information.
        Each dictionary has the following keys:
            - username (str): The username of the user.
            - task (str): The title of the task.
            - completed (bool): Indicates whether the task is completed or not
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
