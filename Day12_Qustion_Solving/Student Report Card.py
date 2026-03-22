
name = input("Enter Your Name: ")
math = int(input("Enter Your Maths Marks: "))
phy = int(input("Enter Your Physics Marks: "))
It = int(input("Enter Your IT Marks: "))
chem = int(input("Enter Your Chemistry Marks: "))
eng = int(input("Enter Your English Marks: "))


data = {
    name : {
        "Maths": math,
        "Physics" : phy,
        "IT" : It,
        "Chemistry" : chem,
        "English" : eng,
    }
}
total = 500
total_sum = float(math + phy + It + chem + eng)
Percentage = (total_sum/total)*100
if 90 <= Percentage <= 100:
    print(f"Congratulations 🎉 you got Grade A with a percentage of {Percentage}%.")
elif 80 <= Percentage <= 89:
    print(f"Great 🎉 you got Grade B with a percentage of {Percentage}%.")
elif 70 <= Percentage <= 79:
    print(f"Nice 🎉 you got Grade C with a percentage of {Percentage}%.")
else:
    print(f"You got Grade D with a percentage of {Percentage}%.")
for student_name, subjects in data.items():
    print(f"---Report Card of {student_name}---")
    for subject, marks in subjects.items():
        print(f"{subject} = {marks}")