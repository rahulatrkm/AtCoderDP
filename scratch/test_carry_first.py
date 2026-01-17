"""
Test: What if we carry forward BEFORE processing queries?
"""
from collections import defaultdict

def simple_dp_carry_first(n, queries):
    by_right = defaultdict(list)
    for l, r, a in queries:
        by_right[r].append((l, a))
    
    dp = [0]*(n+1)
    print(f"Initial: dp = {dp}\n")
    
    for i in range(n):
        print(f"=== Position {i} ===")
        
        # Carry forward FIRST
        if i + 1 <= n:
            old_val = dp[i+1]
            dp[i+1] = max(dp[i+1], dp[i])
            if old_val != dp[i+1]:
                print(f"Carry: dp[{i+1}]: {old_val} → {dp[i+1]}")
        
        # Then process queries
        if i in by_right:
            old_dp = dp[:]
            for l, a in by_right[i]:
                print(f"Query [{l}, {i}] → {a:+d}")
                prev_best = max(old_dp[0:l]) if l > 0 else 0
                print(f"  prev_best = max(old_dp[0:{l}]) = {prev_best}")
                new_val = prev_best + a
                print(f"  new_val = {new_val}")
                
                for j in range(l + 1, i + 2):
                    old = dp[j]
                    dp[j] = max(dp[j], new_val)
                    if old != dp[j]:
                        print(f"  dp[{j}]: {old} → {dp[j]}")
        
        print(f"After: dp = {dp}\n")
    
    return max(0, dp[n])

# Test case
n = 3
queries = [(0, 2, 100), (0, 0, -10), (1, 1, -20), (2, 2, -30)]

print("=" * 70)
print("TESTING: CARRY FORWARD FIRST, THEN PROCESS QUERIES")
print("=" * 70)
print()

result = simple_dp_carry_first(n, queries)
print(f"Result: {result}")
print(f"Expected: 90")
print()

# Verify with brute force
def brute_force(n, queries):
    max_score = 0
    best_config = ""
    for mask in range(1 << n):
        config = [(mask >> i) & 1 for i in range(n)]
        score = 0
        for l, r, a in queries:
            if any(config[i] == 1 for i in range(l, r + 1)):
                score += a
        if score > max_score:
            max_score = score
            best_config = ''.join(map(str, config))
    print(f"Brute force: {max_score} (config: {best_config})")
    return max_score

brute_force(n, queries)
