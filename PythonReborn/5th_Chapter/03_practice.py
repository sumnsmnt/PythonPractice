# Question1: Can we have a set with 18 (int) and '18' (str) as a value in it?

# Question2: What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

s = set()
s.add(18)
s.add("18")
print(s, len(s))

# Set evaluate int and float as a same number if the main value is equal.
# Like here 20 & 20.0 both are mathematically equal.
s.add(20)
s.add(20.0)
s.add("20")
print(s, len(s))