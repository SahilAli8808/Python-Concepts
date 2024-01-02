# using for loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(len(numbers)):
#     print(i, end=" ")
# for _ in range(len(numbers)):
#     print("hello", end=" ")
#----------------------------------------------------------
# use of two var in loop
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}

# Iterate over key-value pairs
for key, value in student_scores.items():
    print(f"{key}'s score is {value}")