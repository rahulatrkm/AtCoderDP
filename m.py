'''
ps - https://atcoder.jp/contests/dp/tasks/dp_m
'''

from functools import lru_cache
import sys

sys.setrecursionlimit(10**5)

# @lru_cache(None)
def helper(idx, k):
    # mod = 10**9+7
    # if idx == -1:
    #     if k == 0:
    #         return 1
    #     else:
    #         return 0
    # ans = 0
    # for i in range(min(arr[idx], k)+1):
    #     ans += helper(idx-1, k-i)
    # return ans%mod

    n = len(arr)
    mod = 10**9 + 7
    dp = [[0]*(k+1) for _ in range(n+1)]
    cumsum = [[0]*(k+2) for _ in range(n+1)]

    dp[0][0] = 1
    for j in range(k+1):
        cumsum[0][j+1] = cumsum[0][j] + dp[0][j]

    for i in range(1, n+1):
        for j in range(k+1):
            # Sum dp[i-1][j-c] for c in range(min(arr[i-1], j) + 1)
            # This is sum from max(0, j-arr[i-1]) to j
            left = max(0, j - arr[i-1])
            right = j
            dp[i][j] = (cumsum[i-1][right+1] - cumsum[i-1][left]) % mod
        
        # Build cumsum for row i
        for j in range(k+1):
            cumsum[i][j+1] = (cumsum[i][j] + dp[i][j]) % mod

    return dp[n][k]
            
n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(helper(n-1, k))