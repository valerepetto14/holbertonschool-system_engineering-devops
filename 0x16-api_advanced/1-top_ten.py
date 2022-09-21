#!/usr/bin/python3
"""top_ten"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    try:
        url = "http://reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
        headers = {
            "User-Agent": "My User Agent 1.0"
        }
        data = requests.get(url, headers=headers)
        for i in range(10):
            print(data.json()["data"]["children"][i]["data"]["title"])
    except Exception as e:
        print(None)
