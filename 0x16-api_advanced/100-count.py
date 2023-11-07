#!/usr/bin/python3
""" Queries Reddit API and prints the top
        ten hot posts of a subreddit
"""
import re
import requests
import sys


def add_title(dictionary, hot_posts):
    """ Appends item into a list """
    if len(hot_posts) == 0:
        return

    title = hot_posts[0]['data']['title'].split()
    for word in title:
        for key in dictionary.keys():
            c = re.compile("^{}$".format(key), re.I)
            if c.findall(word):
                dictionary[key] += 1
    hot_posts.pop(0)
    add_title(dictionary, hot_posts)


def recurse(subreddit, dictionary, after=None):
    """ Queries Reddit API """
    u_agent = 'Mozilla/5.0'
    headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) \
              AppleWebKit/537.36 (KHTML, like Gecko) \
              Chrome/117.0.0.0 Safari/537.36"}

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    dic = res.json()
    hot_posts = dic['data']['children']
    add_title(dictionary, hot_posts)
    after = dic['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, after=after)


def count_words(subreddit, word_list):
    """ Init function """
    dictionary = {}

    for word in word_list:
        dictionary[word] = 0

    recurse(subreddit, dictionary)

    lis = sorted(dictionary.items(), key=lambda kv: kv[1])
    lis.reverse()

    if len(lis) != 0:
        for item in lis:
            if item[1] is not 0:
                print("{}: {}".format(item[0], item[1]))
    else:
        print("")
