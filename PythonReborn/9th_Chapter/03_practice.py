# Write a program to generate multiplication tables from 1 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.

def gen_tab(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)


for i in range(1, 21):
    gen_tab(i)