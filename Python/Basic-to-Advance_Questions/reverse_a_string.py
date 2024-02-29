# Problem Statement:
# Write a Python function that takes a string as input and returns the reverse of that string.

# Input:
# A string s.

# Output:
# Return the reverse of the input string s.
# For example, if the input string is "hello", the output should be "olleh".

str = 'hello'
bag=""
for i in range(len(str)-1,-1,-1):
    bag += str[i]
print (bag)    
