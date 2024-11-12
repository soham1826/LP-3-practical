# Fibonacci number using recursion  
def fibonacci(n): 
    if n <= 1: 
        return n 
    else: 
        return fibonacci(n-1) + fibonacci(n-2)

# Input from the user
n = int(input("Enter number of terms: "))

# Check if the input is valid
if n <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(fibonacci(i))
