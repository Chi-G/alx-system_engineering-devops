#!/usr/bin/python3
"""
This module contains a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords.
"""

import requests

def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords.

    Args:
        subreddit: A string representing the subreddit name.
        word_list: A list of keywords to count.
        after: A string representing the 'after' parameter for pagination (default is None).
        word_count: A dictionary to store word counts (default is an empty dictionary).

    Returns:
        None
    """
    if not word_list:
        return

    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])

        for child in children:
            title = child['data']['title'].lower().split()
            for word in word_list:
                word = word.lower()
                if word in title:
                    word_count[word] = word_count.get(word, 0) + title.count(word)

        after = data.get('after')
        if after:
            count_words(subreddit, word_list, after, word_count)
        else:
            sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_word_count:
                print("{}: {}".format(word, count))
    else:
        return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
        sys.exit(1)
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
