__author__ = 'MacUser'

import create_post
import sys

print("Welcome to the team 3 team challenge! \n")
print("To interact with our application, use the following commands \n")
print("1. 'primfeed view_feed' - to look at the posts made \n")
print("2. 'primfeed post <title> <body>' - to create a post \n")
print("3. 'primfeed comment <postId> <title> <body>`' to make a comment to "
      "the post with an id=postId \n")

print("What would you like to do")

arguments = sys.argv[1:]

if len(arguments) == 2 and arguments[0] == "primfeed" and arguments[1] == "view_feed":

if len(arguments) == 4 and arguments[0] == "primfeed" and arguments[1] == "post":
    returned = create_post.create_post(arguments[3], arguments[4])
    if returned is True:
        print("Thanks for your post! It's been added successfully")
    elif returned is False:
        print("Something went wrong, please give it another shot")
    else:
        print(returned)
    exit()

if len(arguments) == 5 and arguments[0] == "primfeed" and arguments[1] == "comment":
    if isinstance(arguments[2], int):
        print( create_post.create_post(arguments[3], arguments[4]))
    else:
        print("We need the postId to be valid, please try again")
    exit()