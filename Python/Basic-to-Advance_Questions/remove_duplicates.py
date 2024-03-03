# Title - Remove Duplicates from Sorted Array

# Problem Statement:
# Write a Python function that takes a sorted list of integers as input and removes any duplicate elements in-place such that each element appears only once, and returns the length of the modified list. Do not allocate extra space for another list; you must do this by modifying the input list in-place with O(1) extra memory.

# Input:
# A sorted list of integers nums.

# Output:
# Return the length of the modified list after removing duplicates.

# Note: The input list nums is sorted in non-decreasing order.

# For example:
# If the input list is [1, 1, 2, 2, 3, 3, 3, 4], the function should modify the list to become [1, 2, 3, 4] and return 4.

# -----> 1st Method <-----
# Time Complexity (TC): O(n)
# The time complexity is O(n) because it iterates through the entire input list to create the dictionary of unique elements.

# Space Complexity (SC): O(n)
# The space complexity is also O(n) because it creates a dictionary to store unique elements, where the size of the dictionary is proportional to the number of unique elements in the input list.

def remove_duplicates(sorted_list):
    obj = {}
    for num in sorted_list:
        obj[num] = 0;
    return len(obj.keys())

print (remove_duplicates([1, 1, 2, 2, 3, 3, 3, 4]))


# -----> 2nd Method <-----
# Time Complexity (TC): O(n)
# The time complexity is O(n) because it iterates through the entire input list once with two pointers to remove duplicates in-place.

# Space Complexity (SC): O(1)
# The space complexity is O(1) because it modifies the input list in-place without using any additional space proportional to the input size. It only uses a constant amount of extra space for loop variables and index tracking.

def remove_duplicates(sorted_list):
    if not sorted_list:
        return 0

    write_index = 1
    for i in range(1, len(sorted_list)):
        if sorted_list[i] != sorted_list[i - 1]:
            sorted_list[write_index] = sorted_list[i]
            write_index += 1

    return write_index

# Test the function
input_list = [1, 1, 2, 2, 3, 3, 3, 4]
modified_length = remove_duplicates(input_list)
print("Modified list:", input_list[:modified_length])
print("Length of modified list:", modified_length)
