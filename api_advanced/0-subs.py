#!/usr/bin/python3
"""
Reddit Subreddit Subscribers Query Module

This module contains a function that interacts with the Reddit API
to fetch the total number of subscribers for a specified subreddit.
If the subreddit is valid, the function returns the subscriber count.
For an invalid subreddit or any errors during the API request, the
function gracefully returns 0.

Utilizing the Reddit API usually doesn't necessitate authentication
for most operations. To prevent potential "Too Many Requests" issues,
a distinctive User-Agent header is embedded in the request.

Usage:
    1. Ensure the 'requests' module is installed.
    2. Invoke the 'number_of_subscribers(subreddit)' function with
       the desired subreddit name to obtain the subscriber count.

Parameters:
    subreddit (str): The name of the subreddit for which to obtain
    the subscriber count.

Returns:
    int: The number of subscribers for the specified subreddit.
    Returns 0 for invalid subreddits or in the case of errors.

Example:
    subscribers_count = number_of_subscribers("programming")
    print(f"The subreddit 'programming' boasts {subscribers_count} subscribers.")
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to retrieve the total number of subscribers
    (not including active users) for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the specified subreddit.
        Returns 0 for invalid subreddits or in case of errors.
    """
    # Reddit API endpoint for subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Set a unique User-Agent to mitigate potential issues
    headers = {'User-Agent': 'SubredditQueryAgent/1.0'}

    try:
        # Make the API request
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract and return the number of subscribers
            return data['data']['subscribers']
        elif response.status_code == 404:
            # Invalid subreddit returns status code 404
            return 0
        else:
            # Handle other response codes if needed
            print(f"Error: {response.status_code}")
            return 0
    except Exception as e:
        print(f"Error: {e}")
        return 0

# Test the function
if __name__ == '__main__':
    subreddit_name = input("Enter a subreddit: ")
    print(number_of_subscribers(subreddit_name))
