#!/usr/bin/python3
"""
    Script to gather TODO's of an employee using employee ID
"""
from requests import get
from sys import argv

DATA_ENDPOINT = "https://jsonplaceholder.typicode.com"
EMPLOYEE_ID = argv[1]
TASK_TITLES = []


def get_user():
    """
        gets the details of a user
    """
    response = get(url=f"{DATA_ENDPOINT}/users/{EMPLOYEE_ID}")
    data = response.json()
    user_name = data['name']
    return user_name

def get_todos():
    """
        queries the endpoint for user's todo list
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
        f"Employee {get_user()} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):"
        )
    for title in TASK_TITLES:
        print(f"\t {title}")

if __name__ == "__main__":
    get_todos()