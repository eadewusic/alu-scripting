#!/usr/bin/python3
'''
Queries the Reddit API and prints the titles of the first 10 hot posts
for a given subreddit.
'''

import requests

def top_ten(subreddit):
    '''
    Prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
    '''
    # Check if the subreddit is None or not a string
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    # Base URL for the Reddit API
    endpoint = 'https://www.reddit.com'

    # Custom User-Agent to avoid potential issues
    headers = {'user-agent': 'Mozilla/5.0 \
(Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}

    # Make a GET request to the subreddit's hot.json endpoint
    # allow_redirects=False to prevent automatic redirection
    response = requests.get('{}/r/{}/hot.json?limit=10'.format(
            endpoint,
            subreddit), headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract and print the titles of the first 10 hot posts
        for post in data.get('data', {}).get('children', []):
            print(post.get('data', {}).get('title'))
    else:
        # Print None for invalid subreddit or if there's an
        # issue with the request
        print(None)

# Example usage or testing code
if __name__ == '__main__':
    # Test the function with a subreddit (e.g., 'programming')
    subreddit_name = input("Enter a subreddit: ")
    top_ten(subreddit_name)
