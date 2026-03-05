try:
    flr=open("demo.txt","w+")
    flr.write("hello world!\n")
    flr.write("i am karthik\n")
    flr.seek(0)
    temp=flr.read()
    print(temp)
    lst_lines=["from CSE\n","Roll no:24331A05D3\n"]
    flr.writelines(lst_lines)
    flr.seek(0)
    x=flr.readline()
    print(x)
    y=flr.readline()
    print(y)
    flr.seek(0)
    z=flr.readlines()
    print(z)
except FileNotFoundError:
    print("file does not exist")
flr.close()

