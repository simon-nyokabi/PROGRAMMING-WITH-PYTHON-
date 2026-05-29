students = ["Ali", "Buse", "Can", "Derin", "Ece", "Fatih", "Gül"]
scores   = [72, 45, 88, 91, 60, 34, 77]

average_score = round(sum(scores)/len(scores),1)
highest_score = max(scores)
index = scores.index(highest_score)
passed_students = [student for student, score in zip(students, scores) if score >= 60]

for student, score in zip(students, scores):
    print(f'{student} : {score}')

print(f'Average score: {average_score}')
print(f'Highest score : {students[index]}:{scores[index]}')
print(f'Passed Students:{passed_students}')
print(f'Sorted scores :{sorted(scores, reverse=True)}')
