'''
ps - https://atcoder.jp/contests/dp/tasks/dp_p
'''
# from functools import lru_cache
# import sys
# sys.setrecursionlimit(10**7)

def helper(adj):
    mod = 10**9+7

    # @lru_cache(None)
    # def dp(node, col, par):
    #     ans = 1
    #     if col == 0:
    #         for ne in adj[node]:
    #             if ne == par:
    #                 continue
    #             ans *= dp(ne, 1, node)
    #         return ans
    #     for ne in adj[node]:
    #         if ne == par:
    #             continue
    #         ans *= (dp(ne, 0, node) + dp(ne, 1, node))
    #     return ans

    dp = [[0, 0] for _ in range(len(adj)+1)]
    def dfs(node, par):
        dp[node][0] = 1
        dp[node][1] = 1
        for ne in adj[node]:
            if ne == par:
                continue
            dfs(ne, node)
            dp[node][0] = (dp[node][0] * dp[ne][1]) % mod
            dp[node][1] = (dp[node][1] * (dp[ne][0] + dp[ne][1])) % mod

    dfs(1, -1)
    return (dp[1][0] + dp[1][1]) % mod

n = int(input())
edges = []
for _ in range(n-1):
    a, b = map(int, input().split())
    edges.append((a, b))
adj = {}
for i in range(1, n+1):
    adj[i] = []
for a, b in edges:
    adj[a].append(b)
    adj[b].append(a)

print(helper(adj))