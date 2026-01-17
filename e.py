'''
ps - https://atcoder.jp/contests/dp/tasks/dp_e
'''

def solve():
    n, W = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(n)]
    
    max_value = sum(v for _, v in items)
    INF = float('inf')
    
    dp = [INF] * (max_value + 1)
    dp[0] = 0
    
    for w, v in items:
        for j in range(max_value, v - 1, -1):
            dp[j] = min(dp[j], dp[j - v] + w)
    
    ans = 0
    for v in range(max_value + 1):
        if dp[v] <= W:
            ans = v
    
    print(ans)

solve()