
__author__ = 'MacUser'

import create_post, Post_and_comments, commenting_on_post
import sys

print("Welcome to the Primitive News Feed App! \n")
print("To interact with our application, use the following commands \n")
print("1. 'primfeed view_feed' - to look at the posts made \n")
print("2. 'primfeed post <title> <body>' - to create a post \n")
print("3. 'primfeed comment <postId> <title> <body>`' to make a comment to "
      "the post with an id=postId \n")

arguments = sys.argv[1:]

if len(arguments) == 1 and arguments[0] == "view_feed":
    returned = Post_and_comments.get_posts()

    for post in returned:
        idd = ""
        title = ""
        body = ""
        author = ""
        if "id" in post:
            idd = str(post["id"])
        if "title" in post:
            title = str(post["title"])
        if "body" in post:
            body = str(post["body"])
        if "author" in post:
            author = str(post["author"])
        print("ID.: " + idd + " - " + title+"\n")
        print("\n" + body)
        print("By: " + author + "\n\n")


if len(arguments) == 3 and arguments[0] == "post":
    returned = create_post.create_post(arguments[1], arguments[2])
    if returned is True:
        print("Thanks for your post! It's been added successfully")
    elif returned is False:
        print("Something went wrong, please give it another shot")
    else:
        print(returned)
    exit()


if len(arguments) == 4 and arguments[0] == "comment":
    if commenting_on_post.post_comment(arguments[3], arguments[2], arguments[1]):
        print("Thanks for your comment! It's been added successfully")
    else:
        print("Something went wrong, please give it another shot")
    exit()




