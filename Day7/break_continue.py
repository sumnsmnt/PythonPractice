# Break used to terminate the loop when encountered

i = 0

while i <= 10:
    print(i)
    if(i == 5):
        break
    i += 1


# Continue terminates execution in the current iteration & continue execution of the
# loop with the next iteration.
i = 0
while i <= 10:
    if(i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1
    
