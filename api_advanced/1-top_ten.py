#!/usr/bin/python3
"""
Defines a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot articles (default=[]).

    Returns:
        list: A list containing the titles of all hot articles.
              Returns None if no results are found or if the subreddit is invalid.
    """
    if not subreddit or not isinstance(subreddit, str):
        return None

    # Reddit API endpoint for hot articles in the specified subreddit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'my_user_agent'}

    try:
        # Make the API request
        response = requests.get(url, headers=headers)
        data = response.json()

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract titles from the current page and append to hot_list
            titles = [post['data']['title'] for post in data['data']['children']]
            hot_list.extend(titles)

            # Check if there are more pages (pagination)
            after = data['data'].get('after')
            if after:
                # Recursively call the function for the next page
                recurse(subreddit, hot_list, after)

            return hot_list
        elif response.status_code == 404:
            # Invalid subreddit returns status code 404
            return None
        else:
            # Handle other response codes if needed
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Test the function
if __name__ == '__main__':
    subreddit = input("Enter a subreddit: ")
    result = recurse(subreddit)
    if result is not None:
        print(len(result))
    else:
        print("None")
