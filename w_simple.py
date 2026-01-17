'''
Problem W - Intervals: Simple DP solution without segment tree

Time: O(n²) - slower than segment tree but much simpler
Space: O(n)

Algorithm:
- dp[i] = max score achievable considering positions 0..i
- For each position, decide: place '0' or '1'
- If we place '1' at position i, it activates all queries containing i
'''

def solve(n, queries):
    from collections import defaultdict
    
    # Group queries by their right endpoint
    by_right = defaultdict(list)
    for l, r, a in queries:
        by_right[r].append((l, a))
    
    # dp[i] = max score when we've processed positions 0..i-1
    dp = [0] * (n + 1)
    
    # Process each position from left to right
    for i in range(n):
        # Option 1: Don't place '1' at position i
        # Carry forward the score
        dp[i + 1] = max(dp[i + 1], dp[i])
        
        # Option 2: For queries ending at position i, try placing '1' anywhere in [l, i]
        if i in by_right:
            for l, a in by_right[i]:
                # Query is [l, i], we can place '1' at any position in this range
                # Best score before position l
                best_before = max(dp[0:l+1]) if l >= 0 else 0
                new_score = best_before + a
                
                # Update all positions [l+1, i+1] that benefit from this query
                for j in range(l + 1, i + 2):
                    dp[j] = max(dp[j], new_score)
    
    return max(0, dp[n])


n, m = map(int, input().split())
queries = []
for _ in range(m):
    l, r, a = map(int, input().split())
    queries.append((l-1, r-1, a))

print(solve(n, queries))
