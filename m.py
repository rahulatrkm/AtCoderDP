'''
ps - https://atcoder.jp/contests/dp/tasks/dp_m
'''

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    MOD = 10**9 + 7
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    cumsum = [[0] * (k + 2) for _ in range(n + 1)]
    
    dp[0][0] = 1
    for j in range(k + 1):
        cumsum[0][j + 1] = cumsum[0][j] + dp[0][j]
    
    for i in range(1, n + 1):
        for j in range(k + 1):
            left = max(0, j - arr[i - 1])
            dp[i][j] = (cumsum[i - 1][j + 1] - cumsum[i - 1][left]) % MOD
        
        for j in range(k + 1):
            cumsum[i][j + 1] = (cumsum[i][j] + dp[i][j]) % MOD
    
    print(dp[n][k])

solve()