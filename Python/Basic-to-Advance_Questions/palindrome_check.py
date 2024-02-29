# Problem Statement:
# Write a Python function to check if a given string is a palindrome or not. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.

# Input:
# A string s.

# Output:
# Return True if the input string s is a palindrome, and False otherwise.

# For example:
# "racecar" is a palindrome.
# "Hello" is not a palindrome.

# 1st Method
# Time Complexity (TC): O(n)
    # The time complexity is O(n) because it involves creating a reversed copy of the input string using string slicing (s[::-1]), which takes linear time proportional to the length of the string n.
# Space Complexity (SC): O(n)
    # The space complexity is also O(n) because it stores a reversed copy of the input string in memory.
# Output : Hello is Not Palindrome

def is_palindrome(s):
    original_str = s
    reversed_str = s[::-1]

    if (original_str == reversed_str):
        print (f"{s} is Palindrome")
    else:
        print (f"{s} is Not Palindrome")
    
is_palindrome('Hello')


# ---> 2nd Method <---
# Time Complexity (TC): O(n)
    # The time complexity is O(n) because it iterates over half of the input string length (n/2) to compare characters from both ends of the string.
# Space Complexity (SC): O(1)
    # The space complexity is O(1) because it doesn't require any additional space proportional to the input size. It only uses a constant amount of extra space for loop variables.
# Output : racecar is Palindrome

def is_palindrome(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True

# Test the function
if is_palindrome('racecar'):
    print("racecar is Palindrome")
else:
    print("racecar is Not Palindrome")
