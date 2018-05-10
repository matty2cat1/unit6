#Matt Westelman
#5/10/18
#longestWord.py

file = open('engmix.txt')

longestWord=''
for line in file:
    if len(line) > len(longestWord):
        line=longestWord
print(longestWord)
