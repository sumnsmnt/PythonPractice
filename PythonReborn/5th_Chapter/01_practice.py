# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

words = {
    "pani": "water",
    "ladka": "boy",
    "mukka": "punch",
    "pasand": "like",
    "prem": "love"
}

word = input("Enter the word for translation: ")

print(words[word])