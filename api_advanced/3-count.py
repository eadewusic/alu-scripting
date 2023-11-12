#!/usr/bin/python3
'''a recursive function that queries the Reddit API,
 parses the title of all hot articles, and prints a
 sorted count of given keywords
'''
import requests


def count_words(subreddit, word_list, fullname="", count=0, hash_table={}):
    '''Fetches all hot posts in a subreddit and counts
     occurrences of keywords.

    Parameters:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        fullname (str): Identifier for the last post fetched.
        count (int): Count of posts fetched.
        hash_table (dict): Dictionary to store keyword counts.

    Returns:
        None: If subreddit is invalid.
    '''
    # Check for valid input parameters
    if subreddit is None or not isinstance(subreddit, str) or \
       word_list is None or word_list == []:
        return

    # Reddit API endpoint for fetching hot posts
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    params = {'after': fullname, 'count': count}
    headers = {'user-agent': 'Mozilla/5.0 \
(Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}

    # Make a request to the Reddit API
    info = requests.get(url, headers=headers,
                        params=params, allow_redirects=False)

    # Check if the request was successful
    if info.status_code != 200:
        return None

    # Parse the JSON response
    info_json = info.json()

    # Extract the list of posts from the response
    results = info_json.get('data').get('children')
    new_packet = [post.get('data').get('title') for post in results]

    # Count occurrences of keywords in each post
    for title in new_packet:
        for word in word_list:
            word = word.lower()
            formatted_title = title.lower().split(" ")
            if word in formatted_title:
                if word in hash_table.keys():
                    hash_table[word] += 1
                else:
                    hash_table[word] = 1

    # Get the identifier of the last post and update count
    after = info_json.get('data').get('after', None)
    dist = info_json.get('data').get('dist')
    count += dist

    # If there are more posts, recursively call the function
    if after:
        count_words(subreddit, word_list, after, count, hash_table)
    else:
        # Print the sorted count of keywords when all posts are processed
        {print('{}: {}'.format(key, value)) for
         key, value in sorted(hash_table.items(), key=lambda i: (-i[1], i[0]))}
