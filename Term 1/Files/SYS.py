import sys
sys.stdout.write("Enter name of file: ")
file=sys.stdin.readline()
f=open(file.strip(),'r+')
while True:
    ch=f.read(1)
    if ch=="":
        sys.stdout.write("EOL")
        break
    else:
        print(ch,end="")