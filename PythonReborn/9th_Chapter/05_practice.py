# Write a program to mine a log file and find out whether it contains ‘python’.
"""
with open("log.txt", "r") as f:
    log = f.read()

if("python" in log):
    print("Python is present")
else:
    print("Python is not present in the log")
"""

# Write a program to find out the line number where python is present.

with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if ("python" in line):
        print(f"Python is present at line {lineno}")
        break
    lineno += 1

else:
    print("Python is not present")