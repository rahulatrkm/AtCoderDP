'''
Problem W - Intervals: Segment tree solution WITHOUT lazy propagation

Uses simpler segment tree with:
- Point update: set dp[i] = value
- Range query: get max(dp[l..r])

Time: O(m * n * log n) - slightly slower but simpler
Space: O(n)
'''

def solve(n, queries):
    from collections import defaultdict
    
    # Group queries by their right endpoint
    by_right = defaultdict(list)
    for l, r, a in queries:
        by_right[r].append((l, a))
    
    # Simple segment tree for range max query and point update
    class SegmentTree:
        def __init__(self, n):
            self.n = n
            self.tree = [0] * (4 * n)
        
        def update(self, v, tl, tr, pos, val):
            """Set position pos to max(current, val)"""
            if tl == tr:
                self.tree[v] = max(self.tree[v], val)
                return
            
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(2*v, tl, tm, pos, val)
            else:
                self.update(2*v+1, tm+1, tr, pos, val)
            
            self.tree[v] = max(self.tree[2*v], self.tree[2*v+1])
        
        def query(self, v, tl, tr, l, r):
            """Get max value in range [l, r]"""
            if l > r:
                return 0
            if l == tl and r == tr:
                return self.tree[v]
            
            tm = (tl + tr) // 2
            return max(
                self.query(2*v, tl, tm, l, min(r, tm)),
                self.query(2*v+1, tm+1, tr, max(l, tm+1), r)
            )
    
    st = SegmentTree(n + 2)
    
    # Process each position from left to right
    for i in range(n):
        # Carry forward: dp[i+1] = max(dp[i+1], dp[i])
        if i + 1 <= n:
            prev = st.query(1, 0, n, i, i)
            st.update(1, 0, n, i + 1, prev)
        
        # For queries ending at position i
        if i in by_right:
            for l, a in by_right[i]:
                # If we place a '1' anywhere in [l, i], we get score 'a'
                # Best previous score is max(dp[0..l])
                prev_best = st.query(1, 0, n, 0, l) if l >= 0 else 0
                new_val = prev_best + a
                
                # Update all positions in [l+1, i+1] with this new possibility
                for j in range(l + 1, i + 2):
                    st.update(1, 0, n, j, new_val)
    
    return max(0, st.query(1, 0, n, 0, n))


n, m = map(int, input().split())
queries = []
for _ in range(m):
    l, r, a = map(int, input().split())
    queries.append((l-1, r-1, a))

print(solve(n, queries))
