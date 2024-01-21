#!/usr/bin/python3
"""
    Script to get the title of top ten posts in a subreddit.
"""
import requests

def top_ten(subreddit):
    """
        Function that retrieves titles of the top ten posts in a subreddit
    """
    # Set a custom User-Agent to avoid Too Many Requests issues
    headers = {'User-Agent': 'webapp:localhost:v1 (by /u/bappa)'}

    # Reddit API endpoint for getting hot posts in a subreddit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            subreddit_data = response.json()

            # Extract and print the titles of the first 10 hot posts
            for post in subreddit_data['data']['children'][:10]:
                print(post['data']['title'])
        elif response.status_code == 404:
            # Subreddit not found, print None
            print(None)
        else:
            # Handle other errors
            print(f"Error: {response.status_code}")
            print(None)

    except Exception as e:
        # Handle exceptions
        print(f"Exception: {e}")
        print(None)

