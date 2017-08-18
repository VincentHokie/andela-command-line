import view_feed

print(20*">" + "Welcome to the Primitive News Feed App!" + 20*"<" )

print(25*">" + "Here is the available feed:" + 25*"<"  )

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
    print(10*">" + "Id: " + id + " - " + title)
    print(2*"\n" + 15*">" + body)
    print(2*"\n"  + 15*">" + "By: " + author + 4*"\n")

comment_post_id = input("Enter the Id of the post you would like to comment on:\n")
