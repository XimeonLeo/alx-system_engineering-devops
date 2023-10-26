#!/usr/bin/python3
""" Queries the Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) \
              AppleWebKit/537.36 (KHTML, like Gecko) \
              Chrome/117.0.0.0 Safari/537.36"}
    r = requests.get(url, headers=header).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
