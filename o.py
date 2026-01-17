'''
ps - https://atcoder.jp/contests/dp/tasks/dp_o
'''

from functools import lru_cache

@lru_cache(None)
def helper(idx, curr):
    # curr = set(curr)
    mod = 10**9+7
    # n = len(arr)
    # if idx == n:
    #     return 1
    # ans = 0
    # for i in range(n):
    #     if arr[idx][i] and i not in curr:
    #         curr.add(i)
    #         ans += helper(idx+1, tuple(curr))
    #         curr.remove(i)
    # return ans%mod

    n = len(arr)
    dp = [0]*(1<<n)
    dp[0] = 1
    for mask in range(1<<n):
        x = bin(mask).count('1')
        if x >= n:
            continue
        for j in range(n):
            if arr[x][j] and not (mask & (1<<j)):
                dp[mask | (1<<j)] = (dp[mask | (1<<j)] + dp[mask]) % mod
    return dp[(1<<n)-1]

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
print(helper(0, tuple()))
        