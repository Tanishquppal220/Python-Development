f= open("File_IO\\line.txt", "r")
print(f.tell())
print(f.readline())
print(f.tell())
# print(f.seek(0))
f.seek(0)
print(f.readline())

f.close()