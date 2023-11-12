#!/usr/bin/python3
'''
Defines function that queries the Reddit API and returns the
number of subscribers
'''
import requests


def number_of_subscribers(subreddit):
    '''Queries the Reddit API and returns the number of subscribers.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers. Returns 0 for an invalid subreddit.
    '''
    # Check if the subreddit is None or not a string
    if subreddit is None or not isinstance(subreddit, str):
        return(0)

    # Base URL for the Reddit API
    endpoint = 'https://www.reddit.com'

    # Custom User-Agent to avoid potential issues
    headers = {'user-agent': 'Mozilla/5.0 \
(Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}

    # Make a GET request to the subreddit's about.json endpoint
    # allow_redirects=False to prevent automatic redirection
    info = requests.get('{}/r/{}/about.json'.format(
            endpoint,
            subreddit), headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if info.status_code == 200:
        # Parse the JSON response
        json_info = info.json()
        # Extract and return the number of subscribers from the response
        return(json_info.get('data').get('subscribers'))
    else:
        # Return 0 for invalid subreddit or if there's an
        # issue with the request
        return(0)
