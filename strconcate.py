str1=input("Enter your first name:")
str2=input("Enter your last name:")
result=str1+" "+str2
print("strings after concatenation is:",result)
result=f"{str2}{str1}"
print("string concatenation using f string is:",result)
str3=input("Enter another name:")
str4=input("Enter your branch:")
branch="{} {}".format(str3,str4)
print("string concatenation using format function is:",branch)
