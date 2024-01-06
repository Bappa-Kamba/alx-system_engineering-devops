#!/usr/bin/python3
"""
Script to gather TODO's of an employee using employee ID.

This script retrieves the TODO list of an employee from a JSON API and
exports it to a CSV file.
The employee ID is provided as a command-line argument.

Usage: python3 1-export_to_CSV.py <employee_id>
"""
import csv
from requests import get
from sys import argv

DATA_ENDPOINT = "https://jsonplaceholder.typicode.com"
TASK_TITLES = []


def get_username():
    """
    Get the username of the employee.

    Returns:
        str: The username of the employee.
    """
    employee_id = argv[1]
    response = get(url=f"{DATA_ENDPOINT}/users/{employee_id}")
    data = response.json()
    username = data.get('username')
    return username


def get_todos():
    """
    Query the API endpoint for the employee's TODO list and
    export it to a CSV file.
    """
    employee_id = argv[1]
    response = get(url=f"{DATA_ENDPOINT}/users/{employee_id}/todos")
    data = response.json()
    username = get_username()
    for todo in data:
        TASK_TITLES.append([employee_id, username,
                            todo.get('completed'), todo.get('title')])
    with open(f"{employee_id}.csv", 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerows(TASK_TITLES)


if __name__ == "__main__":
    get_todos()
