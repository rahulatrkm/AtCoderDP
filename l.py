'''
ps - https://atcoder.jp/contests/dp/tasks/dp_l
'''
from functools import lru_cache
import sys

sys.setrecursionlimit(10000)

# @lru_cache(None)
def helper(i, j):
    # if j < i:
    #     return 0
    # if i+1 == j:
    #     return max(arr[i], arr[j])
    # if i == j:
    #     return arr[i]
    # c1 = helper(i+2, j)
    # c2 = helper(i+1, j-1)
    # c3 = helper(i, j-2)
    # return max(arr[i] + min(c1, c2), arr[j] + min(c2, c3))

    dp = [[0]*(n) for _ in range(n)]
    dp[0][0] = arr[0]
    for i in range(1, n):
        dp[i-1][i] = max(arr[i], arr[i-1])
        dp[i][i] = arr[i]

    for length in range(2, n):
        j, k = 0, length
        while k < n:
            dp[j][k] = max(arr[j] + min(dp[j+2][k], dp[j+1][k-1]),
                           arr[k] + min(dp[j+1][k-1], dp[j][k-2]))
            j += 1
            k += 1
    return dp[0][n-1]


n = int(input())
arr = list(map(int, input().split()))
s = sum(arr)
fp = helper(0, n-1)
print(2*fp - s)