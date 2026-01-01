n=int(input("Enter the base of a number to find its power:"))
x=int(input("Enter the power of the number:"))
result=1
for i in range(x):
    result*=n
print(n,"to the power of",x,"is:",result)
