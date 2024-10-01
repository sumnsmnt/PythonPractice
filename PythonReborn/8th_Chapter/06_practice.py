# Write a python function to remove a given word from a list and strip it at the same time.

def rm_strip(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
    

l = ["Suman", "Sujan", "Sajan", "Sagar", "an"]
print(rm_strip(l, "an"))