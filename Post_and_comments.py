import requests
import json

def get_posts(parameter=None):

    print("Here is the available feed:")
    response = {}
    ENDPOINT = "http://34.207.10.230:3000/posts"

    if parameter is not None and isinstance(parameter, int):

        ENDPOINT = "http://34.207.10.230:3000/posts/id=" + parameter
    response = requests.get(ENDPOINT)
    return json.loads(response.text)


def get_comments(parameter=None):
    ENDPOINT = "http://34.207.10.230:3000/comments"
    response = {}

    if parameter is not None and isinstance(parameter, int):
        ENDPOINT = "http://34.207.10.230:3000/comments/postId=" + parameter
    response = requests.get(ENDPOINT)
    return json.loads(response.text)
