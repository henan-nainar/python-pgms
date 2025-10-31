def read_number():
    while True:
        n = input("Enter a number (min 4 digits): ")
        if n.isdigit():
            if len(n) >= 4:
                return int(n)
            else:
                print("Please enter min 4 digits.")
        else:
            print("Invalid input, please enter digits only.")

def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

n = read_number()
print("Original:", n)
print("Reversed:", reverse_number(n))






