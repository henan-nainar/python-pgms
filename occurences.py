a=input("enter a line of text: ")
words=a.split()
count_words=[]
counts=[]
for s in words:
    if s not in count_words:
        count=0
        for i in words:
            if i==s:
                count+=1
        count_words.append(s)
        counts.append(count)
for i in range(len(count_words)):                
    print(count_words[i],':',counts[i])
        
