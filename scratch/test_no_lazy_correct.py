"""
Solution WITHOUT lazy propagation but with correct update logic
"""
from collections import defaultdict

def solve_no_lazy(n, queries):
    by_right = defaultdict(list)
    for l, r, a in queries:
        by_right[r].append((l, a))
    
    # Simple segment tree for range max query
    class SegmentTree:
        def __init__(self, n):
            self.n = n
            self.tree = [0] * (4 * n)
        
        def update(self, v, tl, tr, pos, val):
            """Set position pos to val (not max, just set!)"""
            if tl == tr:
                self.tree[v] = val
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
        
        def get(self, pos):
            """Get value at single position"""
            return self.query(1, 0, self.n, pos, pos)
    
    st = SegmentTree(n + 2)
    
    print(f"Initial state\n")
    
    for i in range(n):
        print(f"=== Position {i} ===")
        
        # Process queries ending at position i
        if i in by_right:
            # Save state before processing queries at this position
            saved_state = {}
            for j in range(n + 1):
                saved_state[j] = st.get(j)
            
            for l, a in by_right[i]:
                print(f"Query [{l}, {i}] → {a:+d}")
                
                # Best previous score is max(dp[0..l]) using SAVED state
                prev_best = max(saved_state[j] for j in range(l + 1)) if l >= 0 else 0
                print(f"  prev_best = {prev_best}")
                
                new_val = prev_best + a
                print(f"  new_val = {new_val}")
                
                # Update range [l+1, i+1]
                for j in range(l + 1, i + 2):
                    current = st.get(j)
                    # Set to max(current, new_val) - this is the update
                    updated = max(current, new_val)
                    st.update(1, 0, n, j, updated)
                    if current != updated:
                        print(f"  dp[{j}]: {current} → {updated}")
        
        # Carry forward: dp[i+1] = max(dp[i+1], dp[i])
        if i + 1 <= n:
            prev = st.get(i)
            curr = st.get(i + 1)
            st.update(1, 0, n, i + 1, max(prev, curr))
        
        print()
    
    return max(0, st.query(1, 0, n, 0, n))

# Test
n = 3
queries = [(0, 2, 100), (0, 0, -10), (1, 1, -20), (2, 2, -30)]

result = solve_no_lazy(n, queries)
print(f"Result: {result}")
print(f"Expected: 90")
