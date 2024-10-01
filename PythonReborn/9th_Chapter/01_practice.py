# Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle'

f = open("poems.txt")
poem = f.read()
if ("Twinkle" in poem):
    print("'Twinkle' is present in 'poems.txt'")
else:
    print("'Twinkle' is not present in 'poems.txt'")

f.close()