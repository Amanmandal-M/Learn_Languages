# Problem Statement
# Write a program to calculate the super digit of a given non-negative integer n. The super digit of a number is obtained by repeatedly summing its digits until a single digit is obtained.

def super_digit(n):
    if n <= 9 :
        return print (n)
    
    n = str(n)
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    n = sum
    return super_digit(n)

super_digit(185) 


# Sample Input
9
15
185

# Sample Output 1
9
6 
5
    