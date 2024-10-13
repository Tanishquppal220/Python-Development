def LCM(a, b):
    """Recursive function to find LCM of two numbers."""
    if a == 0 or b == 0:
        return "Invalid"
    else:
        return a * b // GCD(a, b)


def GCD(a, b):
    """Recursive function to find GCD of two numbers."""
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


x = int(input())
y = int(input())
print(LCM(x, y))
