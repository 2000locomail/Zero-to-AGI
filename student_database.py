maths = int(input("Enter Your Marks in Maths Out of 10: "))
physics = int(input("Enter Your Marks in Physics Out of 10: "))
chemistry = int(input("Enter Your Marks in Chemistry Out of 10: "))
marks = [maths, physics, chemistry]
marks.reverse()
min_marks = min(marks)
marks.remove(min_marks) 
print(f"Lowest mark {min_marks} removed. Remaining: {marks}")
avg = sum(marks) / len(marks)
print(f"Average of remaining subjects: {avg:.2f}")
if (9 <= avg <= 10):
    print("Grade: A")
elif(7 <= avg <= 8):
    print("Grade: B")
else:
    print("Grade: C")

