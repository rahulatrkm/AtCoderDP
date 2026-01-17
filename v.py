'''
ps - https://atcoder.jp/contests/dp/tasks/dp_v
'''
import sys
from collections import defaultdict
sys.setrecursionlimit(200000)

def solve():
    n, m = map(int, input().split())
    adj = defaultdict(list)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    if n == 1:
        print(1)
        return
    
    dp1 = [1] * (n + 1)
    
    def dfs1(node, parent):
        prod = 1
        for child in adj[node]:
            if child != parent:
                dfs1(child, node)
                prod = (prod * dp1[child]) % m
        dp1[node] = (1 + prod) % m
    
    dfs1(1, -1)
    
    ans = [0] * (n + 1)
    
    def dfs2(node, parent, parent_contribution):
        children = [child for child in adj[node] if child != parent]
        k = len(children)
        
        if k == 0:
            ans[node] = parent_contribution
            return
        
        prefix = [1] * (k + 1)
        for i in range(k):
            prefix[i + 1] = (prefix[i] * dp1[children[i]]) % m
        
        suffix = [1] * (k + 1)
        for i in range(k - 1, -1, -1):
            suffix[i] = (suffix[i + 1] * dp1[children[i]]) % m
        
        ans[node] = (parent_contribution * prefix[k]) % m
        
        for i in range(k):
            child = children[i]
            remaining = (parent_contribution * prefix[i] % m * suffix[i + 1]) % m
            node_contribution = (1 + remaining) % m
            dfs2(child, node, node_contribution)
    
    dfs2(1, -1, 1)
    
    for i in range(1, n + 1):
        print(ans[i])

solve()
