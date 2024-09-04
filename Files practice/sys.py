import sys as s
s.stdout.write("Enter name of file:")
file=s.stdin.readline()
f=open(file.strip(),"r")
while True:
    ch=f.readline()
    if ch=='':
        s.stderr.write("End of file reached")
        break
    else:
        print(ch, end='')