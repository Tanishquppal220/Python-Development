n = int(input("Enter the number of rows: "))
m=[]
for i in range(1, n+1):
    a=""
    a=a+str("*"*(2*i-1))
    m.append(a)
# print(m)
for i in range(1, n+1):
    print(" "*(n-i), end="")
    print(m[i-1])
for i in range(1, n):
    print(" "*i, end="")
    print(m[n-i-1])






















# for i in range(1, n+1):
#     for j in range(1,n-i+1):
#         print(" ", end="")
#     for j in range(1, i+1):
#         print(j, end="")
#     for j in range(1, i):
#         print(i-j, end="")
#     print()
# for i in range(1, n):
#     # print spaces before the numbers
#     for j in range(1,i+1):
#         print(" ", end="")
#     for j in range(1,n-i+1):
#         print(j, end="")
#     for j in range(1,n-i):
#         print(n-i-j, end="")
#     print()