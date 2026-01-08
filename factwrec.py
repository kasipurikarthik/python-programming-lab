def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fact(num-1)
n=int(input("Enter any positive integer:"))
print("Factorial of",n,"is",fact(n))
