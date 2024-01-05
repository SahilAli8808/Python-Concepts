"""
Dynamic programming (DP) = ek algorithmic technique
- used in optimization problems ko solve karne me , jaise ki shortest path problems, 
sequence alignment, knapsack problems, etc.

- dp basic idea: agar ek problem ko solve karne me kisi subproblem ka solution repeat ho raha hai,
 toh us subproblem ka solution store karke future me reuse kiya ja sakta hai. 
=======================================================================
 key characteristics:
====================================================================
Optimal Substructure: 
A larger problem can be broken down into smaller, overlapping subproblems.

Overlapping Subproblems: 
The problem can be broken down into subproblems which are reused several times.

================================================================================
Fibonacci Series: 
Nth Fibonacci number ko find karne wala problem.

Grid-based Problems: 
Jaise ki Unique Paths, Minimum Path Sum.

Knapsack Problems: 
0/1 Knapsack, Fractional Knapsack.

Longest Common Subsequence (LCS): 
Dete hai ki do sequences me se kitna common subsequence hai.

Longest Increasing Subsequence (LIS): 
Dete hai ki array me se sabse lamba increasing subsequence kya hai.

Matrix Chain Multiplication: 
Matrix multiplication ke saare possible ways me minimum cost ka calculation.

Coin Change Problem: 
Kaise coins ko combine karke ek specific amount banaya ja sakta hai.

Edit Distance: 
Kaise do strings ko same banaya ja sakta hai through minimum operations.

Substring Problems: 
Jaise ki Longest Palindromic Substring.

Maximum Sum Subarray: 
Jaise ki Kadane's Algorithm.

"""