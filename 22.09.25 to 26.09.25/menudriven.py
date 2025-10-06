while(True):
    print("1.Occurence Of Word\n")
    print("2.Each Character Frequency\n")
    print("3.Display the factor of number\n")
    print("4.Exit\n")

    choice=input("enter your choice:")

    if choice=='1':
        string=input("enter the string:")
        words=string.split()
        count_words=[]
        counts=[]

        for w in words:
            if w not in count_words:
                count=0
                for i in words:
                    if i==w:
                        count+=1
                count_words.append(w)
                counts.append(count)
                
        for l in range(len(count_words)):
            print(count_words[l],' : ',counts[l])

    elif choice=='2':
        words=input("enter a word:")
        count_words=[]
        freqcy=[]

        for w in words:
            if w not in count_words:
                freq=0
                for i in words:
                    if i==w:
                        freq+=1
                count_words.append(w)
                freqcy.append(freq)
                
        for l in range(len(freqcy)):
            print(count_words[l],' : ',freqcy[l])

    elif choice=='3':
         number = int(input("Enter a positive integer: "))
         if number >= 0:
            factors = []
            for i in range(1, number + 1):
                if number % i == 0:
                    factors.append(i)
         print(f"The factors of {number} are: {factors}\n")
                    
    elif choice=='4':
        print("exiting the program")
        exit()

else:
    print("invalid choice")
    

        
