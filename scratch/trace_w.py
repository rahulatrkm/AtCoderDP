"""
Trace through w.py to find the bug
"""
from collections import defaultdict

def helper_debug(n, queries):
    by_right = defaultdict(list)
    for l, r, a in queries:
        by_right[r].append((l, a))
    
    print("by_right:", dict(by_right))
    print()
    
    dp = [0]*(n+1)
    print(f"Initial: dp = {dp}")
    print()
    
    for i in range(n):
        print(f"=== Processing position {i} ===")
        dp[i+1] = max(dp[i+1], dp[i])
        print(f"Carry forward: dp[{i+1}] = max(dp[{i+1}], dp[{i}]) = {dp[i+1]}")
        
        if i in by_right:
            for l, a in by_right[i]:
                print(f"  Query [{l}, {i}] → {a:+d}")
                prev_best = dp[l] if l >= 0 else 0
                print(f"    prev_best = dp[{l}] = {prev_best}")
                new_val = prev_best + a
                print(f"    new_val = {prev_best} + {a} = {new_val}")
                print(f"    Updating dp[{l+1}..{i+1}]")
                for j in range(l + 1, i + 2):
                    old = dp[j]
                    dp[j] = max(dp[j], new_val)
                    if dp[j] != old:
                        print(f"      dp[{j}]: {old} → {dp[j]}")
        
        print(f"After position {i}: dp = {dp}")
        print()
    
    return dp[n]

# Test case
queries = [
    (0, 2, 100),
    (0, 0, -10),
    (1, 1, -20),
    (2, 2, -30),
]

result = helper_debug(3, queries)
print(f"Final answer: {result}")
print(f"Expected: 90")
