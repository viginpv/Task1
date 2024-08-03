def is_prime(number):
    
    if number <= 1:
        return False
    if number == 2:
        return True 
    
  
    for i in range(2, number):
        if number % i == 0:
            return False  
    
    return True  
try:
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"The number {num} is Prime.")
    else:
        print(f"The number {num} is Not Prime.")
except ValueError:
    print("error! Please enter an correct integer.")
