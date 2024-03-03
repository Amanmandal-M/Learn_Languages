# Problem Statement:
# Write a Python function that takes a list of integers and a target integer as input and returns the count of occurrences of the target integer in the list.

# Input:
# A list of integers nums.
# An integer target to count occurrences of.

# Output:
# Return the count of occurrences of target in the list nums.

# For example:
# If the input list is [1, 2, 3, 4, 2, 2, 5] and the target integer is 2, the output should be 3 because 2 occurs three times in the list.


def occurrences (list, target):
    count = 0
    
    for i in list:
        if i  == target:
            count += 1
    return count

print (occurrences ([1, 2, 3, 4, 2, 2, 5, 1], 2))