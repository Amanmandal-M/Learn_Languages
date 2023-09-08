def factorial():
    result = 1
    
    n = int(input('Enter number: '))
    
    if (n < 0):
        return 'Invalid Number please put positive numbers'
        
    
    for i in range(n, 0, -1):
        result *= i
    return result


factorial_number = factorial()
print(factorial_number)