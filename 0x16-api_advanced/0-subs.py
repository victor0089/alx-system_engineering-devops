#!/usr/bin/python3
""" How many subs? """
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'victor/1.0 (by RatioForward4396)'}

    r = requests.get(url, headers=headers, allow_redirects=False)

    print("Response Status Code:", r.status_code)
    print("Response Content:", r.text)

    if r.status_code != 200:
        return 0

    try:
        js = r.json()
    except ValueError:
        return 0

    data = js.get("data")

    if data:
        sub_count = data.get("subscribers")
        if sub_count:
            return sub_count

    return 0
