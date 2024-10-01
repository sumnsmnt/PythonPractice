import re

text = "Let's travel together"
pattern = r"Let"

match = re.match(pattern, text)
if match:
    print("Match Found: ", match.group())
else:
    print("No Match Found")