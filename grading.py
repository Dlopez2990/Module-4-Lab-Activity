grading.py
# Calculating Grades (ok, let me think about this one)
# Write a program that will average 3 numeric exam grades, return an average test
score, a corresponding letter grade, and a message stating whether the student is
passing.
# Average Grade
# 90+ A
# 80-89 B
# 70-79 C
# 60-69 D
# 0-59 F
# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.
# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing
exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: ")) # Corrected the int conversion
exam_three = int(input("Input exam grade three: ")) # Corrected the int conversion
grades = [exam_one, exam_two, exam_three] # Added commas to separate elements
sum = 0
for grade in grades: # Corrected variable name from 'grade' to 'grades'
 sum = sum + grade
avg = sum / len(grades) # Corrected variable name from 'grdes' to 'grades'
if avg >= 90:
 letter_grade = "A"
elif avg >= 80 and avg < 90: # Added a colon at the end of the elif statement
 letter_grade = "B"
elif avg >= 70 and avg < 80: # Corrected the condition for 'C' grade
 letter_grade = "C"
elif avg >= 60 and avg < 70: # Corrected the condition for 'D' grade
 letter_grade = "D"
else: # Removed the unnecessary colon from the last elif statement
 letter_grade = "F"
for grade in grades:
 print("Exam: " + str(grade))
print("Average: " + str(avg)) # Moved this line outside of the loop
print("Grade: " + letter_grade) # Moved this line outside of the loop
if letter_grade == "F": # Corrected the variable name to 'letter_grade' and used '==' for
comparison
 print("Student is failing.")
else:
 print("Student is passing.")
