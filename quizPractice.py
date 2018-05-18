#MW
#QuizPractice.py
#date

list = []

file = open('engmix.txt')

def update(A):
        for line in file:
            line.strip()
            A.append(line)

update(list)
print(list[len(list)/2])