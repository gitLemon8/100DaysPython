student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89]

#sum function
total_exam_score = sum(student_scores)

#replica of sum
sum = 0
for score in student_scores:
    sum += score

#print sum both way
print(sum)
print(total_exam_score)

#max function
max_student_score = max(student_scores)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)
print(max_student_score)