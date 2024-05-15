#!/usr/bin/python3
"""
This module queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """Find subreddits"""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    res = requests.get(url, headers={'User-Agent': 'cap_keth'},
                       allow_redirects=False)
    if res.status_code == 200:
        data = res.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        return None
