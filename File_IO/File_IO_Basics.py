# File Basics
f = open("File_IO\\line.txt","rt")
print(f.readline(), end="")
print(f.readline(), end="")
print(f.readline(), end="")
'''
content = f.read()
for line in f:
    print(line)
'''
f.close()