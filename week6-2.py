str=input("Enter a string\n")
str=str.lower()
str2=''.join(reversed(str))
if str==str2:
    print(str,"is a palindrome")
else:
    print(str,"is not a palindrome")
