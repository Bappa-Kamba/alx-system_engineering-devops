#!/usr/bin/python3
"""
This script gathers TODO's of an employee using employee ID.

The script retrieves the details of a user and their TODO list from an API endpoint.
It then prints the number of completed tasks and the titles of those tasks.

Usage: python3 0-gather_data_from_an_API.py [employee_id]
"""

from requests import get
from sys import argv

DATA_ENDPOINT = "https://jsonplaceholder.typicode.com"
EMPLOYEE_ID = argv[1]
TASK_TITLES = []


def get_user():
    """
    Retrieves the name of the user based on the employee ID.

    Returns:
        str: The name of the user.
    """
    response = get(url=f"{DATA_ENDPOINT}/users/{EMPLOYEE_ID}")
    data = response.json()
    user_name = data['name']
    return user_name


def get_todos():
    """
    Queries the endpoint for the user's todo list and prints the completed
    tasks.

    Prints:
        str: The number of completed tasks and their titles.
    """
    response = get(url=f"{DATA_ENDPOINT}/users/{EMPLOYEE_ID}/todos")
    data = response.json()

    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    for todo in data:
        TOTAL_NUMBER_OF_TASKS += 1
        if todo['completed'] == True:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLES.append(todo['title'])
    print(
        f"Employee {get_user()} is done with tasks(\
{NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):"
    )
    for title in TASK_TITLES:
        print(f"\t {title}")


if __name__ == "__main__":
    get_todos()