import re

text = "I'm going to explore Bangalore"
pattern = r"explore"

search = re.search(pattern, text)
if search:
    print("Pattern Found: ", search.group())
else:
    print("Pattern not found")