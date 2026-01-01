num=int(input("Enter a positive number:"))
temp=num
reverse = 0
while (num > 0):
    digit=num%10
    reverse=reverse*10+digit
    num//=10
if (temp==reverse):
    print(temp,"is a palindrome.")
else:
    print(temp,"is not a palindrome.")

