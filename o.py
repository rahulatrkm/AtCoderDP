'''
ps - https://atcoder.jp/contests/dp/tasks/dp_o
'''

curr = set()
def helper(idx):
    mod = 10**9+7
    # n = len(arr)
    # if idx == n:
    #     return 1
    # ans = 0
    # for i in range(n):
    #     if arr[idx][i] and i not in curr:
    #         curr.add(i)
    #         ans += helper(idx+1)
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
print(helper(0))
        