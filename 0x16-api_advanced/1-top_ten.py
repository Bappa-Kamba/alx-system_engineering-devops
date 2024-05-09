#!/usr/bin/python3
"""
Query Reddit API for titles of top ten posts of a given subreddit
"""
import requests


def top_ten(subreddit):
    """
        return top ten titles for a given subreddit
        return None if invalid subreddit given
    """
    # get user agent
    # https://stackoverflow.com/questions/10606133/ -->
    # sending-user-agent-using-requests-library-in-python
    headers = {'User-Agent': 'My User Agent 1.0'}

    url = "https://www.reddit.com/r/{}/hot?limit=10".format(subreddit)
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        top_ten = r.json().get('data', {}).get('children', [])
        if not top_ten:
            print("None")
        for t in top_ten:
            print(t.get('data').get('title'))
