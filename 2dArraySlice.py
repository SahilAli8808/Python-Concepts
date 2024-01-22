# Create a 2D list (without NumPy)
array_non_np = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Slicing without NumPy using list comprehension
sliced_rows = array_non_np[0:2]  # Slicing rows 0 to 1, all columns
sliced_columns = [row[1:3] for row in array_non_np]  # Slicing all rows, columns 1 to 2
sliced_sublist = [row[0:2] for row in array_non_np[1:3]]  # Slicing rows 1 to 2, columns 0 to 1

# Print the results
print("Sliced Rows:")
print(sliced_rows)

print("\nSliced Columns:")
print(sliced_columns)

print("\nSliced Sublist:")
print(sliced_sublist)

