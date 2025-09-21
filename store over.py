a=int(input("enter the number of range: "))
numbers=[]
for i in range(a):
    num=int(input("enter number: "))
    if num>100:
        numbers.append('over')
    else:
        numbers.append(num)
print(numbers)     
        
