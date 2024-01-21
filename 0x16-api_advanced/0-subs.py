#!/usr/bin/python3
"""
    Script to check subscriber count of a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """
        Function to get count of subscribers in a given subreddit.
    """
    # Set a custom User-Agent to avoid Too Many Requests issues
    headers = {'User-Agent': 'webapp:localhost:/api/v1 (by /u/bappa)'}

    # Reddit API endpoint for getting subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            subreddit_data = response.json()

            # Extract and return the number of subscribers
            return subreddit_data['data']['subscribers']
        elif response.status_code == 404:
            # Subreddit not found, return 0
            return 0
        else:
            # Handle other errors
            print(f"Error: {response.status_code}")
            return 0

    except Exception as e:
        # Handle exceptions
        print(f"Exception: {e}")
        return 0
