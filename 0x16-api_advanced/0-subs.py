#!/usr/bin/python3
"""
Query Reddit API for number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
        return number of subscribers for a given subreddit
        return 0 if invalid subreddit given
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # get user agent
    # https://stackoverflow.com/questions/10606133/ -->
    # sending-user-agent-using-requests-library-in-python
    headers = {'User-Agent': 'My User Agent 1.0'}
    subscribers = 0
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        subscribers = r.json().get('data', {}).get('subscribers')
    return subscribers
