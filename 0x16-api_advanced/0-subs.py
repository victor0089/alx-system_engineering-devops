#!/usr/bin/python3
"""Module thatconsumes theReddit API and returnsthe number ofsubscribers"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns thenumber of subscribers(not
    active users,total subscribers) for a given subreddit.

    If not a validsubreddit, return 0.
    Invalid subreddits mayreturn a redirect to search results. Ensure that
    you are not following redirects.

    Args:
        subreddit (str): subreddit

    Returns:
        int: number of subscribers
    """
    base_url = 'https://www.reddit.com/r/'

    url = '{}{}/about.json'.format(base_url, subreddit)
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    results = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )
    if results.status_code == 200:
        return results.json()['data']['subscribers']
    return 0
