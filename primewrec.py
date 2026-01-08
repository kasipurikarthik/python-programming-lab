def primecheck(x,i=1,count=0):
    if i>x:
        return count
    else:
        if x%i==0:
            count+=1
        return primecheck(x,i+1,count)
n=int(input("Enter a positive integer:"))
if(n==1):
    print("1 is neither prime nor composite")
else:
    primecheck(n)
    if primecheck(n)==2:
        print(n,"is a prime")
    else:
        print(n,"is not a prime")
