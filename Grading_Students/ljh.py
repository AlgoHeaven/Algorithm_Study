grades_count = int(input().strip())
grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i]<38:
            continue
        elif grades[i]%5>2:
            grades[i] += (5-grades[i]%5)
    return grades

print(gradingStudents(grades))