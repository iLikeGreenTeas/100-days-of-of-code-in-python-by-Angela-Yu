student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}

for student in student_scores:
    if student_scores[student] > 90:
        student_grades[student] = "Outstanding"
    elif student_scores[student] > 80:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"