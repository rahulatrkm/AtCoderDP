"""
Test: Track which queries are activated explicitly
"""

def dp_track_activated(n, queries):
    m = len(queries)
    # dp[mask] = max score where mask represents which positions have '1'
    # Too expensive: 2^n states
    
    # Different approach: dp[q] = best score considering queries 0..q-1
    # For each query, decide: activate it or skip it
    # If activate: must place '1' somewhere in [l, r]
    
    # dp[q][i] = max score after q queries, last '1' at position i (or none if i=n)
    dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
    dp[0][n] = 0  # No queries processed, no '1' placed
    
    print(f"Initial: dp[0] = {dp[0]}\n")
    
    for q in range(m):
        l, r, a = queries[q]
        print(f"=== Query {q}: [{l}, {r}] → {a:+d} ===")
        
        # Option 1: Don't activate this query
        # Carry forward all states
        for i in range(n + 1):
            dp[q + 1][i] = max(dp[q + 1][i], dp[q][i])
        
        # Option 2: Activate this query by placing '1' in [l, r]
        for place_at in range(l, r + 1):
            # To place '1' at place_at, consider all previous states
            # where last '1' was before place_at (or no '1')
            for prev_i in range(place_at + 1):
                if dp[q][prev_i] > float('-inf'):
                    # Place '1' at place_at, check which queries it activates
                    score = dp[q][prev_i] + a
                    
                    # Check if this '1' activates any previous queries
                    for prev_q in range(q):
                        l_prev, r_prev, a_prev = queries[prev_q]
                        if l_prev <= place_at <= r_prev:
                            # Oops, this '1' also activates query prev_q
                            # But we might have already counted it!
                            pass
                    
                    dp[q + 1][place_at] = max(dp[q + 1][place_at], score)
        
        print(f"After: dp[{q+1}] = {dp[q+1]}\n")
    
    return max(dp[m])

# This approach is getting complicated because we need to track
# which queries each '1' activates...
print("This approach has issues with tracking query activation...")
print("Let me try a cleaner formulation...\n")

def dp_knapsack_style(n, queries):
    """
    Think of it like knapsack:
    - For each query, decide: activate or not
    - If activate: must place '1' somewhere in [l, r]
    - Track: which positions have '1'
    """
    m = len(queries)
    
    # State: (query_index, set of positions with '1')
    # Too many states...
    
    # Alternative: dp[q][last_pos]
    # = max score after query q, with rightmost '1' at last_pos
    
    INF = float('-inf')
    dp = [[INF] * (n + 1) for _ in range(m + 1)]
    dp[0][n] = 0  # No queries, no '1' placed, score = 0 (use n as "no position")
    
    for i in range(n):
        dp[0][i] = 0  # Can place '1' anywhere initially
    
    print(f"Initial: dp[0] = {dp[0]}\n")
    
    for q in range(m):
        l, r, a = queries[q]
        print(f"=== Query {q}: [{l}, {r}] → {a:+d} ===")
        
        # For each previous state
        for prev_last in range(n + 1):
            if dp[q][prev_last] == INF:
                continue
            
            prev_score = dp[q][prev_last]
            
            # Option 1: Don't use this query
            dp[q + 1][prev_last] = max(dp[q + 1][prev_last], prev_score)
            
            # Option 2: Activate this query
            # Place '1' at some position in [l, r]
            for new_pos in range(l, r + 1):
                # Check: does placing '1' at new_pos activate other queries too?
                # This is the problem - we can't easily track which queries
                # are activated by existing '1's
                pass
        
        print(f"After: dp[{q+1}] = (too complex to track...)\n")
    
    print("This formulation also has issues...\n")

print("=" * 70)
print("THE FUNDAMENTAL PROBLEM")
print("=" * 70)
print()
print("When we iterate by queries and decide 'activate or not',")
print("we face a problem:")
print()
print("If we decide to activate Query [0,2] by placing '1' at position 2,")
print("this '1' might ALSO activate Query [2,2]!")
print()
print("We can't decide queries independently because the '1's we place")
print("for one query affect which other queries activate.")
print()
print("This is why the segment tree solution processes by POSITION:")
print("- At each position, we see which queries END there")
print("- We track: 'best score if we place last 1 before position i'")
print("- When a query ends, we know placing '1' in its range activates it")
print("- The segment tree ensures we correctly account for overlaps")
print()

dp_knapsack_style(3, [(0, 2, 100), (0, 0, -10), (1, 1, -20), (2, 2, -30)])
