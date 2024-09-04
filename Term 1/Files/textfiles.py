#files started
#todo METHOD 1
'''
f=open("text.txt", "r+")
f.write('Hello world \nI am Tanishq Uppal\n')
f.write("How are you?")
f.seek(0)
a=f.read()
print(a)
'''
#todo METHOD 2
'''
with open('Text.txt','r+') as f:
    a=f.read()
    print(a)
'''
#todo read,readline and readlines
"""
f=open('Text.txt','r+')
print("This is output if you use read :",f.read(10),sep='\n')
print("This is output if you use read :",f.read(10),sep='\n')
# f.seek(0)
print("This is output if you use readline :",f.readline(20),sep='\n')
f.seek(0)
print("This is output if you use readlines :",f.readlines(),sep='\n')
f.seek(0)
"""
# ! Output
'''
Hello world
I am Tanishq Uppal

Hello world 
I am Hardik Uppal
'''

#todo Write and Writelines
'''
f=open('Text.txt','w+')
f.writelines(["Hello world","\nI am tanishq Uppal"])
'''
f=open('Text.txt'.strip(""),'r+')
print("This is output if you use read :",f.readline(),sep='\n',end='')
print("This is output if you use read :",f.readline(),sep='\n',end='')
print("End")