#Matt Westelman
#5/10/18
#zzWord.py - what do you mean ZZ Top isn't a word?

file = open('engmix.txt')

for line in file:
    if 'zz' in line:
        print(line)