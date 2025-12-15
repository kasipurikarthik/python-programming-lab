import math
n=int(input("Enter number of side of the polygon:"))
s=float(input("Enter length of side of the polygon:"))
Area=(n*pow(s,2))/(4*math.tan(math.pi/n))
print("area of the polygon with", n," sides is:",Area)
