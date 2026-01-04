'''
ps - https://atcoder.jp/contests/dp/tasks/dp_h
'''

def helper(grid):
    h, w = len(grid), len(grid[0])
    mod = 10**9 + 7
    dp = [[0]*w for _ in range(h)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                continue
            if grid[i][j] == '.':
                cnt = 0
                if i > 0:
                    cnt += dp[i-1][j]
                if j > 0:
                    cnt += dp[i][j-1]
                dp[i][j] = cnt % mod
    return dp[-1][-1]

h, w = map(int, input().split())
grid = []
for _ in range(h):
    grid.append(input().strip())

print(helper(grid))