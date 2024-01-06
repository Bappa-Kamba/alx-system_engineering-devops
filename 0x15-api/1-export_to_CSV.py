#!/usr/bin/python3
"""
    Script to gather TODO's of an employee using employee ID
"""
import csv
from requests import get
from sys import argv

DATA_ENDPOINT = "https://jsonplaceholder.typicode.com"
EMPLOYEE_ID = argv[1]
TASK_TITLES = []


def get_username():
    """
        gets the details of a user
    """
    response = get(url=f"{DATA_ENDPOINT}/users/{EMPLOYEE_ID}")
    data = response.json()
    username = data['username']
    return username


def get_todos():
    """
        queries the endpoint for user's todo list
    """
    response = get(url=f"{DATA_ENDPOINT}/users/{EMPLOYEE_ID}/todos")
    data = response.json()
    username = get_username()
    for todo in data:
        TASK_TITLES.append([EMPLOYEE_ID, username,
                            todo['completed'], todo['title']])
    with open(f"{EMPLOYEE_ID}.csv", 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerows(TASK_TITLES)   


if __name__ == "__main__":
    get_todos()
