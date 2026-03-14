# User input for marks
marks = int(input("Enter your Marks : "))
# Standard Python Ternary Operator: [on_true] if [expression] else [on_false]
result = "Pass" if marks >= 33 else "Fail"
print(f"Result : {result}")