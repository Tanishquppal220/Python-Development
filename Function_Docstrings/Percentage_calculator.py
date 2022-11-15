from logging import PercentStyle


def avg(m, t, a, b, c, d):
    Percentage = str("Your Percentage is ")+str(((a+b+c+d)/(m*t))*100)
    return Percentage


v = avg(
    int(input("Enter Maximum Marks in Each Subject:\n")),
    int(input("Enter No of Subjects:\n")),
    int(input("Enter Marks Of First Subject:\n")),
    int(input("Enter Marks Of Second Subject:\n")),
    int(input("Enter Marks Of Third Subject:\n")),
    int(input("Enter Marks Of Forth Subject:\n")),
)
print(v)
