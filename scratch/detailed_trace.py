"""
Compare w.py and w_correct.py step by step
"""
from collections import defaultdict

# Test case
n, m = 3, 4
queries = [(0, 2, 100), (0, 0, -10), (1, 1, -20), (2, 2, -30)]

print("=" * 70)
print("EXPECTED: 90 (place '1' at position 0: +100 from Q0, -10 from Q1)")
print("=" * 70)
print()

# My simple DP
by_right = defaultdict(list)
for l, r, a in queries:
    by_right[r].append((l, a))

dp = [0]*(n+1)
print("Simple DP trace:")
print(f"Initial: dp = {dp}")

for i in range(n):
    print(f"\n--- Position {i} ---")
    if i in by_right:
        for l, a in by_right[i]:
            print(f"Query [{l}, {i}] → {a:+d}")
            prev_best = max(dp[0:l+1]) if l >= 0 else 0
            print(f"  prev_best = max(dp[0:{l+1}]) = max({dp[0:l+1]}) = {prev_best}")
            new_val = prev_best + a
            print(f"  new_val = {prev_best} + {a} = {new_val}")
            for j in range(l + 1, i + 2):
                old = dp[j]
                dp[j] = max(dp[j], new_val)
                if old != dp[j]:
                    print(f"  dp[{j}]: {old} → {dp[j]}")
    
    if i + 1 <= n:
        old = dp[i+1]
        dp[i+1] = max(dp[i+1], dp[i])
        if old != dp[i+1]:
            print(f"Carry: dp[{i+1}]: {old} → {dp[i+1]}")
    
    print(f"After pos {i}: dp = {dp}")

print(f"\nFinal: {dp[n]}")
print()

# Check what dp[1] represents after position 0
print("=" * 70)
print("ANALYSIS")
print("=" * 70)
print("After position 0: dp[1] should represent 'best score if we place")
print("first 1 at position 0', which activates Query 0 and Query 1.")
print("Expected: dp[1] = 100 + (-10) = 90")
print(f"Actual: dp[1] = {[0, 0, 0, 0] if True else None}")  # Will show from trace above
