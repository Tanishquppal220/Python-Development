import math

# a=math.radians(60)
# print(a)
# print(math.sin(0.523599))

#! finding height
len= float(input("Enter the Length of the tower: "))
ang= float(input("Enter the angle of the tower(in degress): "))
alpha= math.radians(ang)
print("Hypothesisof tower is:",len*(math.sin(alpha)))

