# File I/O in Python
# Python can be used to perform operattions on a file . (read & write data)
# Typed of all files: 
# 1 Text Files : .txt, .docx, .log etc.
# 3 Binary Files : .mp4, .mov, .png, .jpeg etc.

# open, read & close File
# we have to open a file before reading or writing

f = open("G:\Jeax\Pyhon To AGI\Day022\demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

f = open("G:\Jeax\Pyhon To AGI\Day022\demo.txt", "r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close()

f = open("G:\Jeax\Pyhon To AGI\Day022\demo.txt", "w")
rewrite = input("Enter: ")
f.write(rewrite)
f.close()

f = open("Semple.txt", "w")
rewrite = input("Enter: ")
f.write(rewrite)
f.close()

f = open("G:\Jeax\Pyhon To AGI\Day022\demo.txt", "r+")
rewrite = input("Enter: ")
f.write(rewrite)
f.close()