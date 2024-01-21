#!/usr/bin/python3
"""
    Script
"""
import requests


def recurse(subreddit, hot_list=None, after="tmp"):
    """
    Return all hot articles for a given subreddit.
    Return None if an invalid subreddit is given.
    """
    if hot_list is None:
        hot_list = []

    # Set a custom User-Agent to avoid Too Many Requests issues
    headers = {'User-Agent': 'My User Agent 1.0'}

    # Update URL with 'after' parameter if available
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    if after != "tmp":
        url += f'?after={after}'

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json().get('data', {})
            children = data.get('children', [])

            # Append titles to the hot_list
            for child in children:
                title = child.get('data', {}).get('title')
                if title:
                    hot_list.append(title)

            # Recursive call with the next page's 'after' parameter
            after = data.get('after')
            if after:
                recurse(subreddit, hot_list, after)
            else:
                # If there are no more pages, return the accumulated hot_list
                return hot_list
        elif response.status_code == 404:
            # Subreddit not found, return None
            return None
        else:
            # Handle other errors
            print(f"Error: {response.status_code}\nHello")
            return None

    except Exception as e:
        # Handle exceptions
        print(f"Exception: {e}")
        return None

