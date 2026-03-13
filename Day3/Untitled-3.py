# Conditional Statements
light = input("Light : ").lower().strip()
if (light == "red"):
    print("Stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("Go")
else:
    print("light is broken")

marks = int(input("marks : "))
if(marks>=90):
    print("Grade : A")
elif(marks>=80 and marks < 90):
    print("Grade : B")
elif(marks>=70 and marks < 80):
    print("Grade : C")
else:
    print("Grade : D")
