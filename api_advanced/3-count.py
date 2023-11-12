#!/usr/bin/python3
'''
Recursively queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords.
'''

import requests

def count_words(subreddit, word_list, count_dict=None, after=None):
    '''
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        count_dict (dict): A dictionary to store the counts (default is None).
        after (str): The identifier for the last post in the previous page.

    Returns:
        None
    '''
    # Check if the subreddit is None or not a string
    if subreddit is None or not isinstance(subreddit, str):
        return

    # Base URL for the Reddit API
    endpoint = 'https://www.reddit.com'

    # Custom User-Agent to avoid potential issues
    headers = {'user-agent': 'Mozilla/5.0 \
(Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}

    # Parameters for the API request
    params = {'limit': 100, 'after': after}

    # Initialize count_dict if it's None
    if count_dict is None:
        count_dict = {}

    # Make a GET request to the subreddit's hot.json endpoint
    response = requests.get('{}/r/{}/hot.json'.format(endpoint, subreddit),
                            headers=headers, params=params, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract and process the titles
        posts = data.get('data', {}).get('children', [])
        for post in posts:
            title = post.get('data', {}).get('title', '').lower()

            # Check if any keyword is present in the title
            for keyword in word_list:
                # Exclude variations like java. or java! or java_
                keyword = keyword.lower().rstrip('.,!_')
                if keyword in title:
                    # Update the count in count_dict
                    count_dict[keyword] = count_dict.get(keyword, 0) + 1

        # Check if there are more pages (pagination) and recurse
        after = data.get('data', {}).get('after')
        if after is not None:
            count_words(subreddit, word_list, count_dict, after)

    # Print the sorted count of keywords
    print_results(count_dict)

def print_results(count_dict):
    '''
    Prints the sorted count of keywords.

    Args:
        count_dict (dict): A dictionary containing keyword counts.
    '''
    # Sort by count (descending) and then alphabetically (ascending)
    sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))

    # Print the results
    for keyword, count in sorted_counts:
        print(f'{keyword}: {count}')

# Example usage or testing code
if __name__ == '__main__':
    # Test the function with a subreddit and a list of keywords
    subreddit_name = input("Enter a subreddit: ")
    keywords = input("Enter a list of keywords (separated by spaces): ").split()
    count_words(subreddit_name, keywords)