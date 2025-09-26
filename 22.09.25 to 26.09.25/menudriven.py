running = True
while running:
    print("\n--- Menu ---")
    print("1. Word Occurrence")
    print("2. Character Frequency")
    print("3. Factors of a Number")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        a=input("enter the string: ")
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

    elif choice == '2':
        text = input("Enter a string: ")
        
        char_freq = {}
        for char in text:
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9':
                found = False
                for key in char_freq:
                    if key == char:
                        char_freq[key] += 1
                        found = True
                        break
                if not found:
                    char_freq[char] = 1
        
        print("Character Frequencies:")
        for char in char_freq:
            print(f"'{char}': {char_freq[char]}")

    elif choice == '3':
        num_str = input("Enter a number to find its factors: ")
        
        is_valid_num = True
        for char in num_str:
            if not ('0' <= char <= '9'):
                is_valid_num = False
                break
        
        if is_valid_num:
            num = int(num_str)
            if num <= 0:
                print("Please enter a positive integer.")
            else:
                print(f"Factors of {num}:")
                factor = 1
                while factor <= num:
                    if num % factor == 0:
                        print(factor)
                    factor += 1
        else:
            print("Invalid input. Please enter a valid integer.")

    elif choice == '4':
        running = False
        print("Exiting program.")

    else:
        print("Invalid choice. Please try again.")
