def fun(suffix,lst):
    print(suffix,lst[0],"your reg.no is",lst[1],"your college code is",lst[2])
details=list(map(str,input("Enter your details in the order(name,regno,collegename):").split()))
fun("hi",details)
