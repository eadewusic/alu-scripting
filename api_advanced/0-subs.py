#!/usr/bin/python3

"""
Reddit API Subreddit Subscribers Query Module

This module defines a function that queries the
Reddit API to retrieve the number of subscribers
for a given subreddit.

If the subreddit is valid, the function returns
the number of subscribers. If an invalid subreddit
is given or if there are
any errors during the API request, the function returns 0.

The Reddit API does not require authentication for most features
To prevent "Too Many Requests" errors, a custom User-Agent
header is set in the request.

Usage:
    1. Ensure you have the necessary modules installed
    (json, urllib.error, urllib.parse, urllib.request).
    2. Call the `number_of_subscribers(subreddit)`
    function with the desired subreddit name to
    retrieve the subscriber count.

Parameters:
    subreddit (str): The name of the subreddit for
    which you want to retrieve the subscriber count.

Returns:
    int: The number of subscribers for the specified subreddit.
    Returns 0 for invalid subreddits or in case of errors.

Example:
    subscribers = number_of_subscribers("programming")
    print(f"The 'programming' subreddit has {subscribers} subscribers.")

"""
import json
import urllib.error
import urllib.parse
import urllib.request


def number_of_subscribers(subreddit):
    """
    Write a function that queries the Reddit API and returns
    the number of subscribers (not active users, total subscribers)
    for a given subreddit. If an invalid subreddit is given,
    the function should return 0.

    Hint: No authentication is necessary for most features of
    the Reddit API. If you’re getting errors related to Too
    Many Requests, ensure you’re setting a custom User-Agent.

    Requirements:

    Prototype: def number_of_subscribers(subreddit)
    If not a valid subreddit, return 0.
    NOTE: Invalid subreddits may return a redirect to search results.
    Ensure that you are not following redirects.
    """
    # create a url
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # create a request object
    req_object = urllib.request.Request(url, method="GET")
    # create a custom user agent
    req_object.add_header('User-Agent', 'OboloScript/1.0')
    # open the url and send req_object to server and get
    # a response
    try:
        with urllib.request.urlopen(req_object) as res_object:
            res_json = json.JSONDecoder().decode(res_object.
                                                 read().decode("utf-8"))
    except urllib.error.HTTPError:
        return 0
    else:
        return res_json["data"]["subscribers"]
