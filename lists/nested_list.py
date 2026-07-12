# Problem: Nested Lists
# Platform: HackerRank
# Concept: Nested Lists / Sorting

students=[]

for _ in range(int(input())):
    name = str(input())
    score = float(input())
    students.append([name,score])
scores=[]
for student in students:
    scores.append(student[1])
scores=sorted(set(scores))
second_lowest=scores[1]
result=[]
for student in students:
    if student[1]==second_lowest:
        result.append(student[0])
result.sort()
for name in result:
    print(name)
