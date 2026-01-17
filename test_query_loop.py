"""
Test: Outer loop on queries instead of positions
"""

def dp_by_queries(n, queries):
    m = len(queries)
    # dp[q][i] = max score after processing queries 0..q-1, with last '1' at position i (or before)
    # But that's O(m*n) space...
    
    # Try: dp[i] = max score with last '1' at position i or before
    # Process queries one by one, update dp accordingly
    
    dp = [0] * (n + 1)
    print(f"Initial: dp = {dp}\n")
    
    for q_idx, (l, r, a) in enumerate(queries):
        print(f"=== Query {q_idx}: [{l}, {r}] → {a:+d} ===")
        
        new_dp = dp[:]
        
        # Option 1: Don't activate this query (keep all dp values)
        # Already in new_dp
        
        # Option 2: Activate this query by placing '1' somewhere in [l, r]
        for place_at in range(l, r + 1):
            # If we place '1' at position place_at to activate this query
            # Best previous score: max(dp[0..place_at])
            # (positions before or at place_at)
            prev_best = max(dp[0:place_at+1])
            score_with_this = prev_best + a
            
            # Update all positions >= place_at that could benefit
            for i in range(place_at + 1, n + 1):
                new_dp[i] = max(new_dp[i], score_with_this)
        
        dp = new_dp
        print(f"After: dp = {dp}\n")
    
    return max(dp)

# Test case
n = 3
queries = [(0, 2, 100), (0, 0, -10), (1, 1, -20), (2, 2, -30)]

print("=" * 70)
print("APPROACH: ITERATE THROUGH QUERIES")
print("=" * 70)
print()

result = dp_by_queries(n, queries)
print(f"Result: {result}")
print(f"Expected: 90")
