#!/usr/bin/python3
'''A module containing functions for working with the Reddit API.'''
import requests

BASE_URL = 'https://www.reddit.com'
'''Reddit's base API URL.'''

def top_ten(subreddit):
    '''Retrieves the title of the top ten posts from a given subreddit.'''
    api_headers = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
    }
    sort = 'top'
    limit = 10
    url = '{}/r/{}/.json?sort={}&limit={}'.format(BASE_URL, subreddit, sort, limit)
    try:
        res = requests.get(url, headers=api_headers, allow_redirects=False)
        if res.status_code == 200:
            posts = res.json().get('data', {}).get('children', [])
            if not posts:
                print(None)
                return
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException as e:
        print(None)
