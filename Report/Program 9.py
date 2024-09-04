def fibonacci(n):
    a, b = 1, 1
    while a <= n:
        print(a, end=' ')
        a, b = b, a + b


num = int(input("Enter a number: "))
print("Fibonacci sequence up to", num, ":")
fibonacci(num)
