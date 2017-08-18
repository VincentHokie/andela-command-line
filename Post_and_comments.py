import requests


def get_posts(parameter):
    endpoint = "http://34.207.10.230:3000/posts "
    response = requests.get(endpoint)
    if parameter is not None and isinstance(parameter, int):
        endpoint = "http://34.207.10.230:3000/comments/postId=" + parameter
    return response.text


def get_comments(parameter):
    endpoint = "http://34.207.10.230:3000/comments"
    response = requests.get(endpoint)
    if parameter is not None and isinstance(parameter, int):
        endpoint = "http://34.207.10.230:3000/comments/postId=" + parameter
    return response.text
