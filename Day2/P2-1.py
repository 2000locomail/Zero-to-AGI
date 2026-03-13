a = int(input("A : "))
b = int(input("B : "))
c = int(input("C : ")) 
add = (a+b)*c
multi = a+b*c
diff = add - multi
print("Result with Brackets (a+b)*c is:", add)
print("Result with Default Precedence a+b*c is:", multi)
print("The difference between both results is:", diff)
print("Data type of difference is:", type(diff))

