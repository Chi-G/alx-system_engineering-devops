#!/usr/bin/python3
"""
This module queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a given subreddit.
    
    Args:
        subreddit: A string representing the subreddit name.
        
    Returns:
        The number of subscribers for the subreddit, or 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
        sys.exit(1)
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
