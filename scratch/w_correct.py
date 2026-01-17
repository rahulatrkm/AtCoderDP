'''
ps - https://atcoder.jp/contests/dp/tasks/dp_w

Correct solution using DP with lazy propagation segment tree.

Problem: Choose positions to place '1's in a binary string.
For each query (l, r, a): if there's at least one '1' in [l, r], add a to score.
Maximize the total score.

Key insight: 
- dp[i] = max score when the rightmost '1' is at position i (or before)
- For each position i, try placing a '1' there
- Use segment tree to efficiently track score contributions
'''

def solve(n, queries):
    from collections import defaultdict
    
    # Group queries by their right endpoint
    by_right = defaultdict(list)
    for l, r, a in queries:
        by_right[r].append((l, a))
    
    # Segment tree for range max query and range add update
    class LazySegTree:
        def __init__(self, n):
            self.n = n
            self.tree = {}
            self.lazy = {}
        
        def get(self, key):
            return self.tree.get(key, 0)
        
        def get_lazy(self, key):
            return self.lazy.get(key, 0)
        
        def push(self, v, tl, tr):
            if self.get_lazy(v) != 0:
                self.tree[v] = self.get(v) + self.get_lazy(v)
                if tl != tr:
                    self.lazy[2*v] = self.get_lazy(2*v) + self.get_lazy(v)
                    self.lazy[2*v+1] = self.get_lazy(2*v+1) + self.get_lazy(v)
                self.lazy[v] = 0
        
        def update(self, v, tl, tr, l, r, add):
            self.push(v, tl, tr)
            if l > r:
                return
            if l == tl and r == tr:
                self.lazy[v] = self.get_lazy(v) + add
                self.push(v, tl, tr)
                return
            tm = (tl + tr) // 2
            self.update(2*v, tl, tm, l, min(r, tm), add)
            self.update(2*v+1, tm+1, tr, max(l, tm+1), r, add)
            self.push(2*v, tl, tm)
            self.push(2*v+1, tm+1, tr)
            self.tree[v] = max(self.get(2*v), self.get(2*v+1))
        
        def query(self, v, tl, tr, l, r):
            if l > r:
                return 0
            self.push(v, tl, tr)
            if l == tl and r == tr:
                return self.get(v)
            tm = (tl + tr) // 2
            return max(self.query(2*v, tl, tm, l, min(r, tm)),
                      self.query(2*v+1, tm+1, tr, max(l, tm+1), r))
    
    st = LazySegTree(n + 2)
    
    # Process each position from left to right
    for i in range(n):
        # For queries ending at position i
        if i in by_right:
            for l, a in by_right[i]:
                # If we place a '1' anywhere in [l, i], we get score 'a'
                # Best previous score is max(dp[0..l-1])
                prev_best = st.query(1, 0, n, 0, l) if l > 0 else 0
                # Update range [l+1, i+1] by adding (prev_best + a)
                new_val = prev_best + a
                st.update(1, 0, n, l + 1, i + 1, new_val - st.query(1, 0, n, l + 1, l + 1))
        
        # Carry forward: dp[i+1] = max(dp[i+1], dp[i])
        if i + 1 <= n:
            prev = st.query(1, 0, n, i, i)
            curr = st.query(1, 0, n, i + 1, i + 1)
            st.update(1, 0, n, i + 1, i + 1, max(prev, curr) - curr)
    
    return max(0, st.query(1, 0, n, 0, n))


n, m = map(int, input().split())
queries = []
for _ in range(m):
    l, r, a = map(int, input().split())
    queries.append((l-1, r-1, a))

print(solve(n, queries))
