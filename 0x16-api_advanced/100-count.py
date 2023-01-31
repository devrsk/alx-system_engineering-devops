#!/usr/bin/python3
""" a module that parses the title of all hot articles and prints
a sorted count of given keywords  """
import requests


def count_words(subreddit, word_list, after='', sorted_keyword={}):
    """ a method that prints a sorted count of a given keyword """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    agent = {'User-Agent': 'Python/requests'}

    params = {'after': after, 'limit': 100}
    response = requests.get(url, headers=agent, params=params,
                            allow_redirects=False)
    if response.status_code == 404 or response.status_code == 302:
        print("")
        return
    data = response.json().get('data')
    after = data.get('after')
    hot_titles = data.get('children')
    for t in hot_titles:
        title = t.get('data').get('title').lower().split()
        for word in word_list:
            if word.lower() in title:
                count = 0
                for word_title in title:
                    if word_title == word.lower():
                        count += 1
                if sorted_keyword.get(word) is None:
                    sorted_keyword[word] = count
                else:
                    sorted_keyword[word] += count

    if after is not None:
        count_words(subreddit, word_list, after, sorted_keyword)
    else:
        if len(sorted_keyword) == 0:
            print("")
            return
        sorted_keyword = sorted(sorted_keyword.items(),
                                key=lambda x: (-x[1], x[0]))
        for k, v in sorted_keyword:
            print("{}: {}".format(k, v))
