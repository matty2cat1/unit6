#Matt Westelman
#5/10/18
#howManyWords.py - all these words, and yet my vocabulary consists of under 200 words

list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
file = open('engmix.txt')

def update(A):
        for line in file:
            line.strip()
            return([len(line)] = [len(line)+1])
        
print(update(list))
        
    
    
