# Write a program to find out whether a given post is talking about “Suman” or not.

post = input("Enter your post: ")

if ("SUMAN".lower() in post.lower()):
    print("This post is talking about suman")
else:
    print("This post is not talking about suman")