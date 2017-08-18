import requests

def get_posts():
    endpoint = requests.get("http://34.207.10.230:3000/posts")
    if endpoint.status_code != 200:
        raise requests.HTTPError(endpoint, str(endpoint.status_code))
    return endpoint.json()
        
