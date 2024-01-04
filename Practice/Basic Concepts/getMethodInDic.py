#syntax for get:  dictionary.get(keyname, value)
#uses:  to get the value of the item with the specified keyname
#       if the keyname does not exist, return the specified value
#       if the keyname is not specified, return None
#       if the keyname is not specified, and the specified value is not specified, return None
#       if the keyname does not exist, and the specified value is not specified, return None    
#       if the keyname does not exist, and the specified value is specified, return the specified value
#       if the keyname exists, and the specified value is specified, return the value of the keyname
#       if the keyname exists, and the specified value is not specified, return the value of the keyname
#       if the keyname exists, and the specified value is specified, return the value of the keyname
from collections import Counter
# example
# my_list = [1, 2, 3, 1, 2, 1, 4, 5, 4, 2]

# Use Counter to count the frequency of each element in the list
my_list = [1,3,4,1,2,3,1]
frequency_counter = Counter(my_list)
# frequency_counter = {}
# for num in nums:
#     #  1  in [1,3,4,1,2,3,1]
#             frequency_counter[num] = frequency_counter.get(num, 0) + 1 

print(frequency_counter)
min_frequency = min(frequency_counter.values())
print(min_frequency)
# #if any number occurs once in frequency_counter then it will return 1
# print(frequency_counter.values(1))
# key print
# print(frequency_counter.keys())
# # frequency value
# print(frequency_counter.values())

# items_frequency =frequency_counter.items()
# print(items_frequency)


