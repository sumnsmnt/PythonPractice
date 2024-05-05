# Dictionaries are used to store data values in key:values pairs
# They are unordered, mutable & don't allow duplicate keys

info = {"name" : "Suman", 
        "age" : 26, 
        "is_adult" : True,
        "subject" : "Python",
        "topics" : ("dict", "set"),
        "marks" : [69, 84, 75, 93]
        }
print(info)
print(type(info))
print(info["name"])
print(info["age"])

# assign new values
info["name"] = "Suman Samanta"
info["role"] = "DevOps Engineer"

print(info)

# We can create an empty dictionary
null_dict = {}
null_dict["title"] = "Learn with Suman"
print(null_dict)