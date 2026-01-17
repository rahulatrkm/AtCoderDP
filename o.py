'''
ps - https://atcoder.jp/contests/dp/tasks/dp_o
'''

def solve():
    MOD = 10**9 + 7
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    dp = [0] * (1 << n)
    dp[0] = 1
    
    for mask in range(1 << n):
        x = bin(mask).count('1')
        if x >= n:
            continue
        for j in range(n):
            if arr[x][j] and not (mask & (1 << j)):
                dp[mask | (1 << j)] = (dp[mask | (1 << j)] + dp[mask]) % MOD
    
    print(dp[(1 << n) - 1])

solve()