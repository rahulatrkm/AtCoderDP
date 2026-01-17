'''
ps - https://atcoder.jp/contests/dp/tasks/dp_t
'''

from functools import lru_cache
import sys
sys.setrecursionlimit(10000)

# def helper(idx):
#     # print(idx, curr)
#     mod = 10**9 + 7
#     if idx == len(s):
#         return 1
    
#     n = len(s) + 1
#     ans = 0
#     for i in range(idx+1, n):
#         if s[idx] == '<':
#             if curr[idx] < curr[i]:
#                 curr[idx+1], curr[i] = curr[i], curr[idx+1]
#                 ans += helper(idx+1)
#                 curr[idx+1], curr[i] = curr[i], curr[idx+1]
#         else:
#             if curr[idx] > curr[i]:
#                 curr[idx+1], curr[i] = curr[i], curr[idx+1]
#                 ans += helper(idx+1)
#                 curr[idx+1], curr[i] = curr[i], curr[idx+1]
#     return ans % mod

'''
dp(i, j) = number of ways to arrange first i elements 
           where the i-th element is the j-th smallest among them
'''

@lru_cache(None)
def helper_recursive(i, j):
    # Recursive solution - works but O(N³) time
    if i == 1 and j == 1:
        return 1
    if i < 1 or j < 1 or j > i:
        return 0
    ans = 0
    mod = 10**9 + 7
    if s[i-2] == '<':
        for k in range(1, j):
            ans = (ans + helper_recursive(i - 1, k)) % mod
    else:
        for k in range(j, i):
            ans = (ans + helper_recursive(i - 1, k)) % mod
    return ans % mod

def helper():
    # Optimized iterative solution with prefix sums: O(N²) time, O(N) space
    n = len(s) + 1
    mod = 10**9 + 7
    
    # Use only 2 rows for space optimization
    dp = [[0]*(n+1) for _ in range(2)]
    dp[1][1] = 1  # Base: first element is 1st smallest (row 1, not row 0)
    
    for i in range(2, n+1):
        curr = i % 2
        prev = (i - 1) % 2  # Previous row index
        
        # Clear current row
        for j in range(n+1):
            dp[curr][j] = 0
        
        # Build prefix sum array for O(1) range queries
        prefix = [0]*(n+1)
        for j in range(1, i):
            prefix[j] = (prefix[j-1] + dp[prev][j]) % mod
        
        for j in range(1, i+1):
            if s[i-2] == '<':
                # Sum dp[prev][k] for k in [1, j-1]
                if j > 1:
                    dp[curr][j] = prefix[j-1]
            else:  # '>'
                # Sum dp[prev][k] for k in [j, i-1]
                dp[curr][j] = (prefix[i-1] - prefix[j-1] + mod) % mod
    
    # Sum all dp[n][j] for j in [1, n]
    ans = 0
    last = n % 2
    for j in range(1, n+1):
        ans = (ans + dp[last][j]) % mod
    return ans


n = int(input())
s = input().strip()
# ans = 0
# for i in range(1, n+1):
#     ans += helper(n, i)
# print(ans%(10**9 + 7))
print(helper())
