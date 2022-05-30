num1 = input("Enter A number:\n")
num2 = input("Enter Another number:\n")
try:
    print(int(num1)+int(num2))
except Exception as e:
    print(e)
print("This is very simple and easy to understand.\n")