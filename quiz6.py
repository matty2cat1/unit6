#Matt Westelman
#5/21/18
#quiz6.py - Final quiz?

L = []

file = open('engmix.txt')

letter = input("Enter a letter ")

for line in file:
    lettcou = line.count(letter)
    if lettcou == 4:
        print(line)
