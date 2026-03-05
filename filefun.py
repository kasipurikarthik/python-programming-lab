try:
    file = open("demo.txt","r")
    file.seek(9)
    print("Present position: ",file.tell())
    temp=file.read()
    print("After 9 characters: ",temp)
    file1=open("flush","r")
    temp=file1.read()
    print("Before flush: ",temp)
    file1=open("flush","w")
    file.flush()
except FileNotFoundError:
    print("File does not exist..")