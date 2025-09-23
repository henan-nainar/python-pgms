a=input("enter a string: ")
if len(a)>0:
    first_char=a.lower()[0]
    new_string=first_char+a[1:].replace(first_char,'$')
else:
    new_string=""
print(new_string)    
