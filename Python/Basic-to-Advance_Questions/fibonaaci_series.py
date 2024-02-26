# Problem Statement:
# Write a Python function to generate the Fibonacci series up to a specified number of terms. The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.

# Input:
# An integer n, specifying the number of terms in the Fibonacci series to generate.

# Output:
# Return a list containing the Fibonacci series up to the nth term.

# For example, if n is 5, the Fibonacci series would be: [0, 1, 1, 2, 3]

def fibonacci(n):
    fib_series = [0, 1]  # Initialize the series with the first two Fibonacci numbers
    
    if n <= 0:
        return "Invalid input. Please provide a positive integer for the number of terms."
    elif n == 1:
        return [0]  # Return [0] if only one term is requested
    
    while len(fib_series) < n:
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    
    return fib_series[:n]

# Example usage:
num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
fibonacci_series = fibonacci(num_terms)
print("Fibonacci series:", fibonacci_series)
