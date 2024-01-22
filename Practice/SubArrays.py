def distinct_subarrays(arr):
    result = []

    for start in range(len(arr)):
        subarray = set()
        for end in range(start, len(arr)):
            if arr[end] not in subarray:
                subarray.add(arr[end])
                result.append(arr[start:end + 1])

    return result

# Example usage:
input_array = [1, 2, 3, 4]
result_subarrays = distinct_subarrays(input_array)

print("All subarrays of distinct elements:")
for subarray in result_subarrays:
    print(subarray)
