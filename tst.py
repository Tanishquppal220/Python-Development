while True:
    print("====================================")
    print("=              MENU                =")
    print("====================================")
    print("= 1. Generate a table for an input number")
    print("= 2. Find the biggest of 3 input numbers")
    print("= 3. Print the sum of all the numbers in a list")
    print("= 4. Reverse a string")
    print("= 5. Check whether a string is a palindrome or not")
    print("= 6. Calculate the number of uppercase and lowercase letters in a string")
    print("= 7. Exit")
    print("====================================")
    choice = input("Enter your choice: ")
    if choice == '1':
        n = int(input("Enter a number: "))
        for i in range(1, 11):
            print(n, "*", i, "=", n * i)
        print()
    elif choice == '2':
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        c = int(input("Enter a number: "))
        if a > b and a > c:
            print(a, "is the biggest\n")
        elif b > a and b > c:
            print(b, "is the biggest\n")
        else:
            print(c, "is the biggest\n")
    elif choice == '3':
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        sum = 0
        for i in l:
            sum = sum + i
        print(sum)
        print()
    elif choice == '4':
        s = input("Enter a string: ")
        print(s[::-1])
        print()
    elif choice == '5':
        s = input("Enter a string: ")
        if s == s[::-1]:
            print("Palindrome\n")
        else:
            print("Not a palindrome\n")
    elif choice == '6':
        s = input("Enter a string: ")
        uc = 0
        lc = 0
        for i in s:
            if i.isupper():
                uc = uc + 1
            elif i.islower():
                lc = lc + 1
        print("Uppercase letters:", uc)
        print("Lowercase letters:", lc)
        print()
    elif choice == '7':
        break
    else:
        print("Invalid choice. Try again.\n")