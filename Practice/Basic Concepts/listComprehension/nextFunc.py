#next function in list comprehension
# syntax
# next(iterator, default)
# iterator: any iterable object
# default (optional): this value is returned if the iterator is exhausted (there is no next item)
# example
list = [1,2,3,4,5]
# using list comprehension
new_list = [i**2 for i in list]
print(new_list)