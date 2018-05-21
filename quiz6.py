#Matt Westelman
#5/21/18
#quiz6.py - Final quiz?

number = 0

file = open('engmix.txt')

let = input("Enter a letter ")

num = int(input("Enter a number"))


""" PROGRAM 1
for line in file:
    lettcou = line.count(let)
    if lettcou == 4:
        print(line)
"""
""" PROGRAM 2 - I doubt it works though...
for line in file:
    line = line.strip()
    if len(line)==9:
        if line[0] == line[4] == line[8]
        print(line)
        break
"""

""" PROGRAM 3 
for line in file:
    line = line.strip()
    if len(line) == num and line[0] == let:
        print(line)
"""

""" PROGRAM 4
for line in file:
    line = line.strip()
    if len(line) >= 10:
        number+=1
        if number == 8000:
            print(line)
            break
"""

