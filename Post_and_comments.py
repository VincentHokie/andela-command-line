import requests


def get_posts():
    endpoint = "http://34.207.10.230:3000/posts "
    response = requests.get(endpoint)
    return response.text


def get_comments():
    endpoint = "http://34.207.10.230:3000/comments"
    response = requests.get(endpoint)
    return response.text
