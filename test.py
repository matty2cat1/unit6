
#Matt Westelman
#5/9/18
#fileDemo.py - How to read a file

file = open('engmix.txt')

numWords = 0
for line in file:
    if 'west' in line:
        print(line.strip())
    numWords += 1
    
print(numWords)
