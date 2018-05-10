#Matt Westelman 
#5/10/18
#lastWordDemo.py

file = open('fileDemo.py')

for line in file:
    words = line.split()
    if len(words)>0:
        print(words[-1])
    else:
        print()