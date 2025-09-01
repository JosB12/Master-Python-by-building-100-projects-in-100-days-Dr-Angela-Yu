student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

total_exam_score = sum(student_scores)
# print(total_exam_score)
# print(range(1, 10))
#
# sum = 0
# for score in student_scores:
#     sum += score
# print(sum)

# max_score = max(student_scores)
# print(f"{max_score}")

score_number = 0
for score in student_scores:
    if score > score_number:
        score_number = score
print(f"{score_number}")