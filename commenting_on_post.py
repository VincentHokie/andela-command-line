import requests
import json

def post_comment(comment, title, postId):
    '''
    Assumes the post commented on has an ID of 50
    '''

    ENDPOINT = "http://34.207.10.230:3000/comments"
    payload = {"title": title, "body": comment, "postId": postId }
    res = requests.post(ENDPOINT, data=payload)

    data = json.loads(res.text)
    # return true if the request was successful
    if data["title"] == title and data["body"] == comment and data["postId"] == postId:
        return True
    else:
        return False
