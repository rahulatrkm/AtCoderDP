'''
ps - https://atcoder.jp/contests/dp/tasks/dp_g
'''
import sys
from collections import defaultdict
sys.setrecursionlimit(200000)

def solve():
    n, m = map(int, input().split())
    adj = defaultdict(list)
    
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
    
    dp = [-1] * (n + 1)
    
    def dfs(node):
        if dp[node] != -1:
            return dp[node]
        dp[node] = 0
        for neighbor in adj[node]:
            dp[node] = max(dp[node], dfs(neighbor) + 1)
        return dp[node]
    
    ans = 0
    for i in range(1, n + 1):
        ans = max(ans, dfs(i))
    
    print(ans)

solve()