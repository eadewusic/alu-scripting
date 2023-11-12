#!/usr/bin/python3
'''a recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a
sorted count of given keywords
'''
import requests
import copy

def count_words(subreddit, word_list, fullname="", count=0, hash_table=None):
    '''Fetches all hot posts in a subreddit and counts occurrences of keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        fullname (str): Identifier for the last post in the previous page.
        count (int): The total count of posts processed.
        hash_table (dict): A dictionary to store the counts of each keyword.

    Returns:
        None
    '''
    # Check if the subreddit is invalid or input is malformed
    if subreddit is None or not isinstance(subreddit, str) or \
       word_list is None or word_list == []:
        return
    
    # Initialize hash_table if it's None
    if hash_table is None:
        hash_table = {}

    # URL for Reddit API endpoint
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    
    # Parameters for the API request
    params = {'after': fullname, 'count': count}
    
    # Custom User-Agent to avoid potential issues
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    
    # Make a GET request to the subreddit's hot.json endpoint
    info = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    # Check if the request was successful (status code 200)
    if info.status_code != 200:
        return None
    
    # Parse the JSON response
    info_json = info.json()
    
    # Extract the list of posts
    results = info_json.get('data').get('children')
    
    # Extract titles and count occurrences of keywords
    new_packet = [post.get('data').get('title') for post in results]
    for title in new_packet:
        for word in word_list:
            word = word.lower()
            formatted_title = title.lower().split(" ")
            if word in formatted_title:
                # Update or initialize count in the hash_table
                if word in hash_table.keys():
                    hash_table[word] += formatted_title.count(word)
                else:
                    hash_table[word] = formatted_title.count(word)
    
    # Extract pagination information
    after = info_json.get('data').get('after', None)
    dist = info_json.get('data').get('dist')
    count += dist
    
    # If there are more pages, recurse with updated parameters
    if after:
        # Pass a new hash_table to avoid sharing counts between recursive calls
        count_words(subreddit, word_list, after, count, copy.deepcopy(hash_table))
    else:
        # If no more pages, print the results after reaching the end
        {print('{}: {}'.format(key, value)) for key, value in sorted(hash_table.items(), key=lambda i: (-i[1], i[0]))}

# Example usage or testing code
if __name__ == '__main__':
    # Test the function with a subreddit and a list of keywords
    subreddit_name = input("Enter a subreddit: ")
    keywords_input = input("Enter a list of keywords separated by spaces: ")
    keywords = [x for x in keywords_input.split()]

    # Call the count_words function
    count_words(subreddit_name, keywords)
