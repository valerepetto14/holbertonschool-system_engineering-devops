#!/usr/bin/python3
"""def function number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """def function that return subscripter of a subrredit"""
    try:
        url = "http://reddit.com/r/{}/about.json".format("programming")
        headers = {
            "User-Agent": "My User Agent 1.0"
        }
        data = requests.get(url, headers=headers)
        return data.json()["data"]["subscribers"]
    except Exception as e:
        return 0