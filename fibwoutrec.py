def fib(x):
    p=0
    q=1
    print("Fibonacci Series is:")
    for i in range(x):
        print(p,end=" ")
        p,q=q,p+q
n=int(input("Enter number of terms:"))
fib(n)
