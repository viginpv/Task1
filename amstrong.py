def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == number

try:
    num = int(input("Enter a number: "))

  
    if is_armstrong(num):
        print(f"The number {num} is an Armstrong number.")
    else:
        print(f"The number {num} is not an Armstrong number.")
except ValueError:
    print("Invalid input! Please enter an integer.")
