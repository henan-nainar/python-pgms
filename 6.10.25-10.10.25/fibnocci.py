def fibonacci(n):
    if n<=0:
        return
    elif n==1:
        print(0)
        return
    else:
        print("**Fibonacci Series**")
        n1,n2=0,1
        print(n1,end=" ")
        print(n2,end=" ")
        for i in range(2,n):
            n3=n1+n2
            print(n3,end=" ")
            n1=n2
            n2=n3
        print()

n=int(input("enter the range"))
fibonacci(n)
