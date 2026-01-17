'''
ps - https://atcoder.jp/contests/dp/tasks/dp_v
'''

from functools import lru_cache
import collections
import sys
sys.setrecursionlimit(200000)

def helper(n, edges, m):
    adj = collections.defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    @lru_cache(None)
    def dfs(node, col, par):
        # print(node, col, "here")
        vis.add(node)
        if col == 0:
            return 1
        ans = 1
        for ne in adj[node]:
            if ne in vis:
                continue
            ans *= dfs(ne, col, node)
        # print(node, col, ans)
        return ans + 1
    res = []
    for i in range(1, n+1):
        vis = set()
        res.append((dfs(i, 1, -1)-1) % m)
    return res


def helper_bottom_up(n, edges, m):
    """
    Bottom-up solution - cleaner implementation.
    For each node as root, compute product of (1 + child_subtree_value).
    
    Time: O(N^2), Space: O(N)
    """
    adj = collections.defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    def solve(root):
        vis = set()
        
        def dfs(node):
            vis.add(node)
            prod = 1
            for nei in adj[node]:
                if nei not in vis:
                    prod = (prod * dfs(nei)) % m
            return (1 + prod) % m
        
        return (dfs(root) - 1) % m
    
    return [solve(i) for i in range(1, n + 1)]


def helper_tabular(n, edges, m):
    """
    Tabular solution using iterative post-order DFS with explicit stack.
    Uses DP table to store subtree products for each node.
    
    Time: O(N^2), Space: O(N)
    """
    adj = collections.defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    def solve(root):
        # DP table: dp[node] = product of (1 + child_subtree_value)
        dp = [0] * (n + 1)
        visited = [False] * (n + 1)
        
        # Post-order traversal using explicit stack
        stack = [(root, False)]  # (node, processed)
        order = []
        
        while stack:
            node, processed = stack.pop()
            
            if processed:
                # Post-order: process this node after all children
                order.append(node)
            else:
                # First visit: mark and push for post-processing
                visited[node] = True
                stack.append((node, True))
                
                # Push all unvisited children
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        stack.append((neighbor, False))
        
        # Fill DP table in post-order (children before parents)
        for node in order:
            prod = 1
            for neighbor in adj[node]:
                if visited[neighbor] and dp[neighbor] > 0:
                    # This is a child (already processed in post-order)
                    prod = (prod * dp[neighbor]) % m
            dp[node] = (1 + prod) % m
        
        return (dp[root] - 1) % m
    
    return [solve(i) for i in range(1, n + 1)]


def helper_optimized(n, edges, m):
    """
    OPTIMIZED solution using REROOTING DP technique.
    Computes answer for all roots in O(N) time instead of O(N^2)!
    
    Key idea:
    1. First DFS: compute subtree products when node 1 is root
    2. Second DFS: reroot from parent to child, adjusting answers
    
    Time: O(N), Space: O(N)
    """
    if n == 1:
        return [1]
    
    adj = collections.defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # dp1[node] = product when node is considered as subtree (excluding parent)
    dp1 = [1] * (n + 1)
    
    # First DFS: compute subtree products from node 1 as root
    def dfs1(node, parent):
        """Compute dp1[node] = product of (1 + child_subtree)"""
        prod = 1
        for child in adj[node]:
            if child != parent:
                dfs1(child, node)
                prod = (prod * dp1[child]) % m
        dp1[node] = (1 + prod) % m
    
    dfs1(1, -1)
    
    # ans[node] = final answer when node is root
    ans = [0] * (n + 1)
    
    # Second DFS: reroot and compute answers
    def dfs2(node, parent, parent_contribution):
        """
        Reroot from parent to node.
        parent_contribution = what parent contributes when we make 'node' the root
        """
        children = [child for child in adj[node] if child != parent]
        k = len(children)
        
        # Use prefix/suffix products to avoid nested loops
        if k == 0:
            ans[node] = parent_contribution
            return
        
        # Build prefix products
        prefix = [1] * (k + 1)
        for i in range(k):
            prefix[i + 1] = (prefix[i] * dp1[children[i]]) % m
        
        # Build suffix products
        suffix = [1] * (k + 1)
        for i in range(k - 1, -1, -1):
            suffix[i] = (suffix[i + 1] * dp1[children[i]]) % m
        
        # Answer for this node as root
        ans[node] = (parent_contribution * prefix[k]) % m
        
        # Reroot to each child
        for i in range(k):
            child = children[i]
            # Product of all other children + parent contribution
            remaining = (parent_contribution * prefix[i] % m * suffix[i + 1]) % m
            node_contribution = (1 + remaining) % m
            dfs2(child, node, node_contribution)
    
    # Start rerooting from node 1 (no parent contribution initially)
    dfs2(1, -1, 1)
    
    return [ans[i] for i in range(1, n + 1)]


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v)) 
    result = helper_optimized(n, edges, m)
    for val in result:
        print(val)