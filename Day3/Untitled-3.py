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

A = int(input("A : "))
G = input("M/F : ").upper()
if((A == 1 or A == 2) and G == "M"):
    print("fee is 100")
elif((A == 3 or A == 4) and G == "F"):
    print("fee is 200")
elif(A == 5 and G == "M"):
    print("fee is 300")
else:
    print("no fee")