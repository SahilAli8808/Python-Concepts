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

# example
nums = [1,3,4,1,2,3,1]
frequency_counter = {}
for num in nums:
    #  1  in [1,3,4,1,2,3,1]
            frequency_counter[num] = frequency_counter.get(num, 0) + 1 

print(frequency_counter)

# key print
print(frequency_counter.keys())
# frequency value
print(frequency_counter.values())

items_frequency =frequency_counter.items()
print(items_frequency)


