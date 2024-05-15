#!/usr/bin/python3
"""
This module queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    numbers of subscribers
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    res = requests.get(url, headers={'User-Agent': 'cap_keth'},
                       allow_redirects=False)
    if res.status_code == 200:
        return res.json()['data']['subscribers']
    else:
        return 0
