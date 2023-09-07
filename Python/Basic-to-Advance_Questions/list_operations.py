# Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.

data = [1,8,9,52,0,52,8,52,10,55,8962]

data.append(808)
data.remove(0)
sorted_data = sorted(data)
count_data = data.count(52)
data.pop(5)
data.insert(9)
print(data)
