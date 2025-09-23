inp= input("Enter a string: ")
if len(inp) > 0:
    first_char = inp[0]
    result_string = first_string = ''
    
    # Check if string has characters more than 1
    if len(inp) > 1:
        # Loop through the string starting from the second character
        for i in range(1, len(input_string)):
            if input_string[i] == first_char:
                result_string += '$'
            else:
                result_string += input_string[i]
        
    print("Original string:", input_string)
    # Concatenate the first character with the result_string
    print("Modified string:", first_char + result_string)
else:
    print("The string is empty.")

