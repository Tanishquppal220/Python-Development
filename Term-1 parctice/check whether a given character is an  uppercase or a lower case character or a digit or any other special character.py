a=int(input("Enter a character: "))
a=int(chr(a))
if a>=65 and a<=90:
    print("The character is an uppercase letter")
elif a>=97 and a<=122:
    print("The character is a lowercase letter")
elif a>=48 and a<=57:
    print("The character is a digit")
else:
        print("The character is a special character")
