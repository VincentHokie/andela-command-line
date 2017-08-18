__author__ = 'MacUser'

import requests
import json


def create_post(title, body):

    # return error message if the title is non-existent
    if title is None or title.strip() == "":
        return "We need the title to make a post"

    # return error message if the body is non-existent
    if body is None or body.strip() == "":
        return "We need the body to make a post"

    # post the feed
    r = requests.post('http://34.207.10.230:3000/posts',
                      {"title": title, "body": body})

    data = json.loads(r.text)

    # return true if the request was successful
    if data["title"] == title and data["body"] == body:
        return True
    else:
        return False