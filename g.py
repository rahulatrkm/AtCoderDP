'''
ps - https://atcoder.jp/contests/dp/tasks/dp_g
'''
from collections import defaultdict
import sys
sys.setrecursionlimit(200000)

def helper(n, edges):
    dp = [0]*n

    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)

    vis = set()
    def dfs(node):
        if node in vis:
            return dp[node]
        vis.add(node)
        max_path = 0
        for neighbor in adj[node]:
            max_path = max(max_path, dfs(neighbor) + 1)
        dp[node] = max_path
        return dp[node]
    
    for i in range(n):
        dfs(i)
    return max(dp)

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u-1, v-1))
print(helper(n, edges))
        