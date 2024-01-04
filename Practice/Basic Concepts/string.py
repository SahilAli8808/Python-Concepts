S = "12345"
# if '0' not in S and '1' not in S and '2' not in S:
#     print("yes")
# else:
#     print("no")
def smallestSubstring(S):
       # Write your code here
    print(S)
    if '1' not in S :
        return True
    if '0' not in S or '1' not in S or '2' not in S:
        return 0
    
print(smallestSubstring(S))