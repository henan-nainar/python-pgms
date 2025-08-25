a=int(input("enter any positive number: "))
factorial=1
if a>0:
     for i in range (1,a+1):
         factorial=factorial*i
     print("factorial is =",factorial)
else:
    print("invalid")
