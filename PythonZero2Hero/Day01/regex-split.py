import re

text = "Bhubaneswar/Vizag/Ongole/Bangalore"
pattern = r"/"

print(re.split(pattern, text))