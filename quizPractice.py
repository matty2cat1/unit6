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
            L.append(len(L))=len(L+1)

update(list)
print(list[len(list)/2])
print(len(L))