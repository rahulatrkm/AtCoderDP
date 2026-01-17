'''
ps - https://atcoder.jp/contests/dp/tasks/dp_b
'''

def solve():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    
    dp = [float('inf')] * n
    dp[0] = 0
    
    for i in range(1, n):
        for j in range(1, min(k, i) + 1):
            dp[i] = min(dp[i], dp[i-j] + abs(h[i] - h[i-j]))
    
    print(dp[-1])

solve()
