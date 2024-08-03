def sum_of_digits(number):
    total = 0
    number = abs(number)
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    
    return total

num = int(input("Enter a number: "))
result = sum_of_digits(num)
print(f"The sum of the digits of {num} is {result}.")
