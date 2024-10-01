# Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class Demo:
    a = 1

o = Demo()
print(o.a)

o.a = 2
print(o.a)

print(Demo.a)

# So, the class attribute doesn't change.