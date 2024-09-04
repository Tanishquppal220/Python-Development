import random
M=[10,20,30]
while True:
    print(random.randrange(M[0],M[len(M)-1]+1,10))
    if input("Press Enter to continue:"):
        break