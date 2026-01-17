'''
ps - https://atcoder.jp/contests/dp/tasks/dp_c
'''

def solve():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    
    dp = [[0] * 3 for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + points[i-1][0]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + points[i-1][1]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + points[i-1][2]
    
    print(max(dp[n]))

solve()