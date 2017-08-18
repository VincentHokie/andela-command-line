import view_feed

print("Welcome to the Primitive News Feed App!")

print("Here is the available feed:")

for post in view_feed.get_posts():
    id = ""
    title = ""
    body = ""
    author = ""
    if "id" in post.keys():
        id = str(post["id"])
    if "title" in post.keys():
        title = str(post["title"])
    if "body" in post.keys():
        body = str(post["body"])
    if "author" in post.keys():
        author = str(post["author"])
    print("No.: " + id + " - " + title)
    print("\n" + body)
    print("By: " + author + "\n\n")