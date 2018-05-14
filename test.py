#Matt Westelman
#5/9/18
#fileDemo.py - How to read a file

list= []
file = open('fileDemo.py')

for line in file:
    list.append(line.strip())
    
for i in range (len(list)):
    print(list[i] "!")
