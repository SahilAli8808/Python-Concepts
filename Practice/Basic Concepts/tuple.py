r = 4
c = 3
arr = [
    [1, 0, 0],
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
seen =[]

for i in range(r):
    print(arr[i])
    if arr[i] not in seen:
        seen.append(arr[i])
        print(seen)
