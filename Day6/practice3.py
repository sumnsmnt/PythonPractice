# WAP to enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary and add one by one.
# use subject name as key & marks as value.

user = {}

a = int(input("Enter Mathematics: "))
user.update({"math" : a})

b = int(input("Enter Physics: "))
user.update({"phy" : b})

c = int(input("Enter Bio: "))
user.update({"bio" : c})

print(user)