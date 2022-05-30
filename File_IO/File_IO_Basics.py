# File Basics
f = open("File_IO\\Text.txt", "rt")

# content = f.read()
for line in f:
    print(line)

f.close()