import re

text = "Let's travel together"
pattern = r"to"

search = re.search(pattern, text)
if search:
    print("Pattern Found: ", search.group())
else:
    print("Pattern not found")