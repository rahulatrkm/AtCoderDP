"""
Trace w_correct.py with debug output
"""
from collections import defaultdict

def solve(n, queries):
    # Group queries by their right endpoint
    by_right = defaultdict(list)
    for l, r, a in queries:
        by_right[r].append((l, a))
    
    # Simulate segment tree with simple array for debugging
    dp = [0] * (n + 2)
    
    print(f"Initial: dp = {dp}")
    print()
    
    # Process each position from left to right
    for i in range(n):
        print(f"=== Position {i} ===")
        
        # For queries ending at position i
        if i in by_right:
            for l, a in by_right[i]:
                print(f"Query [{l}, {i}] → {a:+d}")
                # Best previous score is max(dp[0..l])
                if l > 0:
                    prev_best = max(dp[0:l+1])  # dp[0..l] inclusive
                    print(f"  prev_best = max(dp[0:{l+1}]) = max({dp[0:l+1]}) = {prev_best}")
                else:
                    prev_best = 0
                    print(f"  prev_best = 0 (l=0)")
                
                new_val = prev_best + a
                print(f"  new_val = {prev_best} + {a} = {new_val}")
                
                # Update range [l+1, i+1]
                print(f"  Updating dp[{l+1}:{i+2}]")
                for j in range(l + 1, i + 2):
                    old = dp[j]
                    dp[j] = max(dp[j], new_val)
                    if old != dp[j]:
                        print(f"    dp[{j}]: {old} → {dp[j]}")
        
        # Carry forward: dp[i+1] = max(dp[i+1], dp[i])
        if i + 1 <= n:
            old = dp[i+1]
            dp[i+1] = max(dp[i+1], dp[i])
            if old != dp[i+1]:
                print(f"Carry: dp[{i+1}]: {old} → {dp[i+1]}")
        
        print(f"After pos {i}: dp = {dp}")
        print()
    
    return max(0, max(dp))

# Test case
n, m = 3, 4
queries = [(0, 2, 100), (0, 0, -10), (1, 1, -20), (2, 2, -30)]

result = solve(n, queries)
print(f"Final answer: {result}")
