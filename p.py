'''
ps - https://atcoder.jp/contests/dp/tasks/dp_p
'''
import sys
sys.setrecursionlimit(10**7)

def solve():
    MOD = 10**9 + 7
    n = int(input())
    
    adj = {i: [] for i in range(1, n + 1)}
    for _ in range(n - 1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    
    dp = [[0, 0] for _ in range(n + 1)]
    
    def dfs(node, par):
        dp[node][0] = 1
        dp[node][1] = 1
        for ne in adj[node]:
            if ne == par:
                continue
            dfs(ne, node)
            dp[node][0] = (dp[node][0] * dp[ne][1]) % MOD
            dp[node][1] = (dp[node][1] * (dp[ne][0] + dp[ne][1])) % MOD
    
    dfs(1, -1)
    print((dp[1][0] + dp[1][1]) % MOD)

solve()