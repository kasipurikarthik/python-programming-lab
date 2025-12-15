import math
a=float(input("enter length of first side of the triangle:"))
b=float(input("enter length of second side of the triangle:"))
c=float(input("enter the length of third side of the triangle:"))
s=(a+b+c)/2
Area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("According to the heron's formula the area of triangle is:",Area)