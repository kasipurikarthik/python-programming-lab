import random
temp=open("demo.txt","w")
for i in range(20):
    x=random.randint(1,100)
    temp.write(str(x))
    temp.write("\n")

