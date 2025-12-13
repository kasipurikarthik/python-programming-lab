import math
print("The value of pi is:",math.pi)
r=float(input("enter radius of the circle:"))
print("area of circle of radius ",r," is:",math.pi*pow(r,2))
num=int(input('enter a positive integer:'))
print("square root of the number you entered is:",math.sqrt(num))
op=float(input("enter length of opposite side of a right angled triangle:"))
adj=float(input("enter length of adjacent side of a right angled triangle:"))
x=math.sqrt(op**2+adj**2)
print("length of hypotenuse of the right angled triangle is:",x)
angle=0*math.pi
print("sin(0°)=",math.sin(angle))
print("cos(0°)=",math.cos(angle))
angle=math.radians(30)
print("sin(30°)=",math.sin(angle))
print("cos(30°)=",math.cos(angle))
angle=math.pi/3
print("sin(60°)=",math.sin(angle))
print("cos(60°)=",math.cos(angle))
angle=math.radians(90)
print("sin(90°)=",math.sin(angle))
print("cos(90°)=",math.cos(angle))

