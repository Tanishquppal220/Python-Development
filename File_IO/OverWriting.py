f = open("File_IO\\line.txt", "r+")

# This is the content of line.txt
'''
Hello This some text for experience 
How are you This is a line 
I am fine is the answer for line 
'''
# f.write("\nHello This file is Changed by Python")

print(f.read())


f.close()
