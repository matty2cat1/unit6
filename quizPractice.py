#MW
#QuizPractice.py
#date

list = []
L = []

file = open('engmix.txt')

def update(A):
        for line in file:
            line.strip()
            A.append(line)

for line in file:
    if len(line)>0 and 'r' == line[0]:
            print(line)

update(list)
print(list[len(list)/2])