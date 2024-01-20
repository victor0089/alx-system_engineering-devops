#!/usr/bin/python3
""" How many subs? """
import requests
from requests import get
from sys import argv


def number_of_subscribers(subreddit):
    # Replace these values with your Reddit application details
    client_id = 'E9UcaSW-udVFniBFD8Cf6w'
    client_secret = 'tiSdtSn31T0MlzpPz3ZGyme7VhAuSg'
    user_agent = 'victor (by RatioForward4396)'

    # Reddit API endpoint for subreddit information
    url = 'https://oauth.reddit.com/r/{}/about.json'.format(subreddit)

    # Set up the headers with authentication
    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    headers = {'User-Agent': user_agent}

    # Make a GET request to the API
    response = requests.get(url, headers=headers, auth=auth,
                            allow_redirects=False)

    # Check if the request was successful (status code 200) and not redirected
    if response.status_code == 200 and not response.is_redirect:
        # Parse the JSON response and extract the number of subscribers
        data = response.json()
        subscribers_count = data['data']['subscribers']
        return subscribers_count
    else:
        # Return 0 for invalid subreddit or other errors
        return 0
