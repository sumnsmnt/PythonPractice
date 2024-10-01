# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. 
# Write a program to detect these spams.

spam1 = "Make a lot of money"
spam2 = "buy now"
spam3 = "subscribe this"
spam4 = "click this"

user_input = input("Please write somthing: ")

if (spam1 in user_input or spam2 in user_input or spam3 in user_input or spam4 in user_input):
    print("This is a spam message")
else:
    print("Everything is fine.")