#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""

import requests

def count_words(subreddit, word_list, after='', word_dict=None):
    """Prints a sorted count of given keywords."""
    
    if word_dict is None:
        word_dict = {word.lower(): 0 for word in word_list}

    if not after:
        word_dict_sorted = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in word_dict_sorted:
            if count:
                print('{}: {}'.format(word, count))
        return

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'user-agent': 'redquery'}
    params = {'limit': 100, 'after': after}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json()['data']
        hot_posts = data.get('children', [])
        after_next = data.get('after')

        for post in hot_posts:
            title = post['data'].get('title', '').lower()
            for word in word_dict:
                word_dict[word] += title.split().count(word)

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    count_words(subreddit, word_list, after_next, word_dict)

