# Fibonacci Calculator

def main():
    number_in_sequence = get_input()
    fibonacci_number = get_fibonacci_number(number_in_sequence)
    print(f"{fibonacci_number:,d}")

def get_fibonacci_number(number_in_sequence):
    if(number_in_sequence <= 0):
        return 0
    else:
        fprevprev = 0
        fprev = 1
        value = 1
        for count in range(2, number_in_sequence):
            fprevprev = fprev
            fprev = value
            value = fprev + fprevprev
            
    
        return value

def get_input():
    while True:
        try:
            return int(input("What Fibonacci number do you want to calculate? "))
        except:
            print("That's not an interger")
            pass

main()