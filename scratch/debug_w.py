'''
Debug w.py - understanding the problem and testing
'''

def helper_debug(n, queries):
    print("=" * 60)
    print("DEBUGGING w.py")
    print("=" * 60)
    print(f"n = {n}, queries = {queries}")
    print()
    
    # Build score changes and track which queries affect each position
    vals = [(set(), set()) for _ in range(n)]
    score = [0]*n
    
    print("Processing queries:")
    for i, (l, r, a) in enumerate(queries):
        print(f"  Query {i}: range [{l}, {r}], value = {a}")
        score[l] += a
        vals[l][0].add(i)  # Query i starts at position l
        if r + 1 < n:
            score[r + 1] -= a
            vals[r + 1][1].add(i)  # Query i ends before position r+1
    
    print()
    print("Score deltas:", score)
    print()
    
    # Build prefix information
    prefix = [set() for _ in range(n)]   
    prefix_score = [0]*n
    curr = set() 
    cp = 0
    
    print("Building prefix sums and active queries:")
    for i in range(n):
        curr |= vals[i][0]  # Add queries that start here
        curr -= vals[i][1]  # Remove queries that ended
        prefix[i] = curr.copy()
        cp += score[i]
        prefix_score[i] = cp
        print(f"  Position {i}: active queries = {prefix[i]}, score = {prefix_score[i]}")
    
    print()
    print("Sorted by score (descending):")
    vals_sorted = sorted(zip(prefix_score, prefix, range(n)), 
                        key=lambda x: (x[0], -len(x[1])), reverse=True)
    for ps, s, idx in vals_sorted:
        print(f"  Position {idx}: score={ps}, active={s}")
    
    print()
    print("=" * 60)
    print("THE ISSUE:")
    print("=" * 60)
    print("The algorithm tries to greedily select positions, but:")
    print("1. When you 'use' a query, it affects ALL positions in its range")
    print("2. The greedy approach doesn't properly account for this")
    print("3. This is likely a segment tree or DP problem, not greedy")
    print()
    print("The problem seems to be about selecting a subset of queries")
    print("to maximize the sum, where taking a query adds its value to")
    print("a range but you can only 'collect' from one position per query.")
    print("=" * 60)


# Test case from the problem
n = 5
queries = [(0, 4, 10), (1, 1, 10), (2, 4, 10)]

helper_debug(n, queries)
