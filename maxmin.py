num1=float(input("Enter num1:"))
num2=float(input("Enter num2:"))
num3=float(input("Enter num3:"))
if (num1>num2)&(num1>num3):
    print(num1,"is the maximum number among",num1,num2,num3)
    if(num2>num3):
        print(num3,"is the minimum number among",num1,num2,num3)
    else:
        print(num2,"is the minimum number among",num1,num2,num3)
elif(num2>num3):
    print(num2,"is the greatest number among",num1,num2,num3)
    if(num1>num3):
        print(num3,"is the minimum number among",num1,num2,num3)
    else:
        print(num1,"is the minimum number among",num1,num2,num3)
else:
    print(num3,"is the greatest number among",num1,num2,num3)
    if(num1>num2):
        print(num2,"is the minimum number among",num1,num2,num3)
    else:
        print(num1,"is the minimum number among",num1,num2,num3)
