n=int(input("Enter a positive integer:"))
def primecheck(x):
    if x==1:
        print("1 is neither prime nor composite")
    else:
        count=0
        for i in range (1,int(x/2)+1):
               if x%i==0:
                count+=1
        if count==1:
            print(x,"is a prime number")
        else:
            print(x,"is not a prime number")      
primecheck(n)
