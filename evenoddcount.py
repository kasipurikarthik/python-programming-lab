n=int(input("Enter upto how many numbers you want to check the odd even count:"))
evencount=0
oddcount=0
for i in range(1,n+1):
    if(i%2==0):
        evencount+=1
    else:
        oddcount+=1
print("even numbers count is:",evencount)
print("odd numbers count is:",oddcount)
