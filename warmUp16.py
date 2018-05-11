#Matt Westelman
#5/9/18
#warmUp16.py - M&W

file = open('engmix.txt')

for line in file:
    line = line.strip()
    if 'm' == line[0] and 'w'== line[-1]:
        print(line)

