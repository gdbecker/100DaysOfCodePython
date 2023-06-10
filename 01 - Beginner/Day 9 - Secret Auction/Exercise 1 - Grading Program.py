student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key,value in student_scores.items():
    if value <= 70:
        student_grades[key] = "Fail"
    elif value >= 71 and value <= 80:
        student_grades[key] = "Acceptable"
    elif value >= 81 and value <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif value >= 91 and value <= 100:
        student_grades[key] = "Outstanding"

# 🚨 Don't change the code below 👇
print(student_grades)
