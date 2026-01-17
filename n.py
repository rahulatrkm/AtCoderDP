'''
ps - https://atcoder.jp/contests/dp/tasks/dp_n
'''

from functools import lru_cache

@lru_cache(None)
def helper(i, j):
    # if i == j:
    #     return 0
    # ans = float('inf')
    # for k in range(i, j):
    #     ans = min(ans, helper(i, k) + helper(k+1, j))
    # return ans + sum(arr[i:j+1])

    n = len(arr)
    dp = [[0]*n for _ in range(n)]
    for i in range(n-1):
        dp[i][i+1] = arr[i] + arr[i+1]
    
    for length in range(2, n):
        j, k = 0, length
        while k < n:
            dp[j][k] = float('inf')
            for cut in range(j, k):
                dp[j][k] = min(dp[j][k], dp[j][cut] + dp[cut+1][k])
            dp[j][k] += sum(arr[j:k+1])
            j += 1
            k += 1
    return dp[0][n-1]


n = int(input())
arr = list(map(int, input().split()))
print(helper(0, n-1))

# n = 400
# arr = [10**9]*n
# print(helper(arr))