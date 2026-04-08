"""# Deleting a file
# using the os module
# Module (like a code library) is a file written by another program that generally has a functions we can use.
import os
f = open("Semple.txt", "w")
rewrite = input("Enter: ")
f.write(rewrite)
f.close()
os.remove("Semple.txt")

# Let's Practice 
# Create a new file "Practice.txt" using python. Add the following data in it:"""
"""
Hi everyone
we are learning File I/O
using java.
I like programming in java.
"""

# replace all occurrences if "java" with "python" in above file.
# Search if the word "learning" exists in the file or not.
def check_for_word():
    with open("practice.txt", "w") as f:
        f.write("Hi everyone \nwe are learning File I/O \nusing java. \nI like programming in java.")

    with open("practice.txt", "r") as f :
        data = f.read()

    new_data = data.replace("java", "Python")
    print(new_data)

    with open("practice.txt", "w") as f :
        f.write(new_data)
    word = "learning"
    with open("practice.txt", "r") as f :
        data = f.read()
        if(data.find(word) != 1):
            print("Found")
        else:
            print("Not Found!")

check_for_word()
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f :
        while data:
            data = f.readline()
            if (word in data):
                print(line_no)
                return
            line_no += 1
    
    return - 1
check_for_line()
