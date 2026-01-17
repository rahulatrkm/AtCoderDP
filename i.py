'''
ps - https://atcoder.jp/contests/dp/tasks/dp_i
'''

def solve():
    n = int(input())
    p = list(map(float, input().split()))
    
    dp = [0.0] * (n + 1)
    dp[0] = 1.0
    
    for i in range(n):
        new_dp = [0.0] * (n + 1)
        for j in range(i + 1):
            new_dp[j] += dp[j] * (1 - p[i])
            new_dp[j + 1] += dp[j] * p[i]
        dp = new_dp
    
    ans = sum(dp[j] for j in range(n // 2 + 1, n + 1))
    print(f'{ans:.10f}')

solve()