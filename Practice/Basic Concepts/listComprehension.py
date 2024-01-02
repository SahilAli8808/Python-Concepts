numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#normal method to create new list ,  contains squares of even numbers from given list.
# for i in numbers:
    
#     #even number
#     if i %2 ==0:
#         # print(i, end=" ")
#         #square of even number
#         square =i**2
#         print(square, end=" ")
# ----------------------------------------------------------

#second method using list comprehension
# new_list = ["hello" for _ in numbers]
# print(new_list)
# ------------------------------------------------------

# new_list = [i**2 for i in numbers if i%2==0]
# print(new_list)
# -----------------------------------------------------------

# creating empty 2d array using of lenth of rows
# new_list = [[] for _ in numbers]
# print(new_list)