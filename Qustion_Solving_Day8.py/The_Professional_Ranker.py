# Project: The Professional Ranker
# Objective: Input marks, sort them descending, and identify ranks

student1 = input("Enter Your Name: ")
student1_marks = int(input(f"Hello, {student1}! Enter Your marks: "))
student2 = input("Enter Your Name: ")
student2_marks = int(input(f"Hello, {student2}! Enter Your marks: "))
student3 = input("Enter Your Name: ")
student3_marks = int(input(f"Hello, {student3}! Enter Your marks: "))
students_marks = [student1_marks, student2_marks, student3_marks]
students_marks.sort(reverse=True)

topper_marks = students_marks[0] 
lowest_marks = students_marks[-1]

print(f"Topper's Score: {topper_marks}")
print(f"Lowest Score: {lowest_marks}")
print("All Sorted Marks:", students_marks)
