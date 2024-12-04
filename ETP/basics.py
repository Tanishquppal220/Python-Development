# Python3 program to convert

# def printRoman(n):
#     num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
#     sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
#     i = len(num)-1
#     s=""

#     while n:
#         a=n//num[i]
#         n %= num[i]
#         s+=sym[i]*a
#         i-=1
#     print(s)

# n = int(input())
# print("Roman value is:", end=" ")
# printRoman(n)

l=[1,2,3,4]
l+=(6,)
print(l)