a=input("enter a string: ")
if len(a)>1:
    new_string=a[-1]+a[1:-1]+a[0]
else:
    new_string=a
print(new_string)    
