#Matt Westelman
#5/16/18
#reverseFile.py - for all intents and purposes, this file has clearly been reversed

list = []
file = open('fileDemo.py')

for line in file:
    line= line.split()
    for word in line:
        word = word.strip()
        print(word[::-1])
    