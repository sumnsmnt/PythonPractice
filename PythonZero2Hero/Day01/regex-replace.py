import re

text = "I'm going to Hyderabad next week"
pattern = r"Hyderabad"

replacement = "Bangalore"

newtext = re.sub(pattern, replacement, text)
print(newtext)