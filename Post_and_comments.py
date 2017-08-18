import requests


def get_posts(parameter):
    ENDPOINT = "http://34.207.10.230:3000/posts"
    if parameter is not None and isinstance(parameter, int):
        ENDPOINT = "http://34.207.10.230:3000/posts/?id=" + parameter
        response = requests.get(ENDPOINT)
    return response.text


def get_comments(parameter):
    ENDPOINT = "http://34.207.10.230:3000/comments"
    if parameter is not None and isinstance(parameter, int):
        ENDPOINT = "http://34.207.10.230:3000/comments/?postId=" + parameter
        response = requests.get(ENDPOINT)
    return response.text
