#!/usr/bin/python3
'''
Recursively queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
'''

import requests

def recurse(subreddit, hot_list=None, after=None):
    '''
    Recursively queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles (default is None).
        after (str): The identifier for the last post in the previous page.

    Returns:
        list: A list containing the titles of all hot articles.
        Returns None if no results are found for the subreddit.
    '''
    # Check if the subreddit is None or not a string
    if subreddit is None or not isinstance(subreddit, str):
        return None

    # Base URL for the Reddit API
    endpoint = 'https://www.reddit.com'

    # Custom User-Agent to avoid potential issues
    headers = {'user-agent': 'Mozilla/5.0 \
(Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}

    # Parameters for the API request
    params = {'limit': 100, 'after': after}

    # Make a GET request to the subreddit's hot.json endpoint
    response = requests.get('{}/r/{}/hot.json'.format(endpoint, subreddit),
                            headers=headers, params=params, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Initialize hot_list if it's None
        if hot_list is None:
            hot_list = []

        # Extract and append the titles to hot_list
        posts = data.get('data', {}).get('children', [])
        for post in posts:
            hot_list.append(post.get('data', {}).get('title'))

        # Check if there are more pages (pagination) and recurse
        after = data.get('data', {}).get('after')
        if after is not None:
            recurse(subreddit, hot_list, after)

        return hot_list
    else:
        # Return None for invalid subreddit or if there's an
        # issue with the request
        return None

# Example usage or testing code
if __name__ == '__main__':
    # Test the function with a subreddit (e.g., 'programming')
    subreddit_name = input("Enter a subreddit: ")
    result = recurse(subreddit_name)
    if result is not None:
        print(len(result))
    else:
        print("None")
