list1=[1,2,3,4,5,6,7]
list2=[6,7,8,9,10,11]
if len(list1)==len(list2):
     print("lists are of same length")
else:
    print("lists are not of same length")
if sum(list1)==sum(list2):
     print("lists are of same sum")
else:
    print("lists are not of same sum")
for i in list1:
    if i in list2:
        print(i," occurs in both")
        
    
