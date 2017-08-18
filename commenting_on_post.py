import requests
import json

def post_comment(comment):
    '''
    Assumes the post commented on has an ID of 50
    '''

    ENDPOINT = "http://34.207.10.230:3000/posts"
    payload = {
       "comments": [{ "title": "My 5 Cents", "body": "{}".format(comment), "postId": 50 }],
    }
    res = requests.post(ENDPOINT, data=json.dumps(payload), headers={'content-Type': 'application/json'})
    print res.text
    print res.status_code


comment = raw_input("Any comments on the blog you just read?   ")
print("Fantastic, thanks for your feedback")

post_comment(comment)

