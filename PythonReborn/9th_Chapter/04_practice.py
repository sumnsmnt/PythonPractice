# A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file. 
'''
word = "Donkey"

with open("donkey.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open ("donkey.txt", "w") as f:
    f.write(contentNew)
'''

# Repeat this program for a list of such words to be censored.

words = ["a", "Monkey", "Donkey"]

with open("donkey.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("donkey.txt", "w") as f:
    f.write(content)