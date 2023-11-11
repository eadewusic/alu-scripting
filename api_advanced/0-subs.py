#!/usr/bin/python3
"""
0-subs

Module to interact with the Reddit API and retrieve the
number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        
    Returns:
        int: The number of subscribers. Returns 0 for an invalid subreddit.
    """
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'my_user_agent'}

    # Reddit API endpoint for subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

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
    subreddit = input("Enter a subreddit: ")
    print(number_of_subscribers(subreddit))
