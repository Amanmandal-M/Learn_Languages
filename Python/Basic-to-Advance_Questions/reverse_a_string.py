# Problem Statement:
# Write a Python function that takes a string as input and returns the reverse of that string.

# Input:
# A string s.

# Output:
# Return the reverse of the input string s.
# For example, if the input string is "hello", the output should be "olleh".

str = 'hello'

### ---> 1st Method <---
# Time Complexity (TC): O(n^2)
# Space Complexity (SC): O(n)

bag=""
for i in range(len(str)-1,-1,-1):
    bag += str[i]
print (bag)   

### ---> 2nd Method <---
# Time Complexity (TC): O(n)
# Space Complexity (SC): O(n)

reversed_str = str[::-1]
print (reversed_str)


# Certainly! Let's break down the expression s[::-1] step by step:
# s: This is the string that we want to reverse. In this case, it's 'hello'.
# [::]: This is called slicing notation in Python. It allows you to extract a portion of a sequence like a string or a list.
# [::-1]: This part specifies the slice of the string and the step size. Let's break it down further:
# :: indicates the start and end of the slice. An empty start and end indices (::) mean we're considering the entire string from the beginning to the end.
# -1 as the step size means we're stepping backward through the string.
# Putting it all together, s[::-1] means "take the entire string s and step backward through it with a step size of -1", effectively reversing the string.
# So, when you assign reversed_str = s[::-1], you're creating a new string reversed_str that contains a reversed copy of the original string s.