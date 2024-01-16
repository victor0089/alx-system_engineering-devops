#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    # Reddit API endpoint for subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    # Set a custom User-Agent to avoid errors related to Too Many Requests
    headers = {'User-Agent': 'CustomUserAgent'}
    
    # Make the GET request
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Get the number of subscribers from the parsed data
        subscribers = data['data']['subscribers']
        
        return subscribers
    elif response.status_code == 404:
        # If subreddit not found, return 0
        print(f"Subreddit '{subreddit}' not found.")
        return 0
    else:
        # Handle other errors
        print(f"Error {response.status_code}: Unable to retrieve data.")
        return 0
