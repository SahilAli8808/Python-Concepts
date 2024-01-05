#list slicing 
# syntax
# list[start:end:step]
# list[start:end]

# example = [1,2,3,4,5,6,7,8,9]
# inder hood the list index is 0,1,2,3,4,5,6,7,8
# nums = [-1,-100,3,99]
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(arr[-2:])
# index  [arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7],arr[8]]
# print(example[0:5:2]) # [start:end:step] its start from 0 and end at 5 and step is 2 and 
#here index 5  is not included we have leave 5 and step is 2 so it will print 1,3,5
# output = [1,3,5]
# for another eg 
# slice k position
# normal
# print(arr[0:10:1])
# 3 index se 7 index tak ke element= [6, 5, 4, 3]
# print(arr[3:7])
#starting se 3 index tak element = [9, 8, 7]
# print(arr[:3])

# ----------------------------------------------
# Basic Slicing:


# # Extract elements from index 2 to 5 (excluding 5)
# sublist = my_list[2:5]
# Omitting Start or Stop:

# python
# Copy code
# # Extract elements from the beginning to index 3 (excluding 3)
# partial_list = my_list[:3]

# # Extract elements from index 5 to the end
# rest_of_list = my_list[5:]
# Using a Step:
# k=2
# n = len(nums)
# left =  nums[k:]
# print("left is", left)
# right = nums[:n-k]
# print(right)
# rotation = left + right
# print(rotation)
        
# python
# Copy code
# # Extract every second element
# every_second = my_list[::2]
# Negative Indices:

# python
# Copy code
# # Extract the last three elements
# last_three = my_list[-3:]
# Reversing a List:

# python
# Copy code
# # Reverse the list
# reversed_list = my_list[::-1]
# Combining Start, Stop, and Step:

# python
# Copy code
# # Extract elements from index 1 to 7, skipping every second element
# complex_slice = my_list[1:7:2]
# Omitting All Indices - Full Copy:

# python
# Copy code
# # Create a full copy of the list
# full_copy = my_list[:]
# Step with Negative Value:

# python
# Copy code
# # Extract elements in reverse order, skipping every second element
# reversed_every_second = my_list[::-2]




