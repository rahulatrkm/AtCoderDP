'''
ps - https://atcoder.jp/contests/dp/tasks/dp_h
'''

def solve():
    MOD = 10**9 + 7
    h, w = map(int, input().split())
    grid = [input().strip() for _ in range(h)]
    
    dp = [[0] * w for _ in range(h)]
    dp[0][0] = 1 if grid[0][0] == '.' else 0
    
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#':
                continue
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
            dp[i][j] %= MOD
    
    print(dp[-1][-1])

solve()