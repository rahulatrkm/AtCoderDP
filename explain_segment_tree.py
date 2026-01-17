"""
Understanding the Segment Tree Solution for Problem W

THE DP STATE:
dp[i] = maximum score when we've processed positions 0..i-1
        (i.e., the best score we can get if position i is available for the next '1')

SEGMENT TREE PURPOSE:
Instead of maintaining a simple array dp[], we use a segment tree that supports:
1. Range Max Query: Find max(dp[l..r]) in O(log n)
2. Range Update: Set dp[l..r] = max(dp[l..r], new_value) in O(log n)
3. Lazy Propagation: Delay updates until needed

PROCESSING ORDER:
We process positions left to right (0 to n-1).
For each position i, we handle queries that END at position i.

WHY THIS ORDER?
When a query (l, r, a) ends at position r:
- We can place a '1' at ANY position in [l, r] to activate it
- We need to know the best score BEFORE position l (to avoid double-counting)

STEP-BY-STEP ALGORITHM:

For each position i from 0 to n-1:
    For each query (l, r, a) ending at position i:
        1. Find best_prev = max(dp[0..l])
           → This is the best score before we activate this query
        
        2. new_score = best_prev + a
           → Score if we place '1' in [l, i] to activate this query
        
        3. Update dp[l+1..i+1] = max(dp[l+1..i+1], new_score)
           → All positions in this range can achieve this score
    
    Carry forward: dp[i+1] = max(dp[i+1], dp[i])
    → Even if we don't place '1' at i, carry the score forward

DETAILED EXAMPLE:
n = 5, positions 0,1,2,3,4
Query 1: [0, 2] → +10
Query 2: [1, 3] → -10
Query 3: [2, 4] → +10

Initial state:
dp = [0, 0, 0, 0, 0, 0]
     ^index 0 represents "no positions used yet"

Position 0 (no queries end here):
- Carry forward: dp[1] = max(dp[0], dp[1]) = max(0, 0) = 0
- State: [0, 0, 0, 0, 0, 0]

Position 1 (no queries end here):
- Carry forward: dp[2] = max(dp[1], dp[2]) = max(0, 0) = 0
- State: [0, 0, 0, 0, 0, 0]

Position 2 (Query 1 ends here: [0, 2] → +10):
- Query 1: l=0, r=2, a=10
  * best_prev = max(dp[0..0]) = 0
  * new_score = 0 + 10 = 10
  * Update dp[1..3] = max(current, 10)
    - dp[1] = max(0, 10) = 10
    - dp[2] = max(0, 10) = 10
    - dp[3] = max(0, 10) = 10
- Carry forward: dp[3] = max(dp[2], dp[3]) = max(10, 10) = 10
- State: [0, 10, 10, 10, 0, 0]

What does this mean?
- dp[1]=10: If we place first '1' at position 0, we get 10 points (Query 1)
- dp[2]=10: If we place first '1' at position 1, we get 10 points (Query 1)
- dp[3]=10: If we place first '1' at position 2, we get 10 points (Query 1)

Position 3 (Query 2 ends here: [1, 3] → -10):
- Query 2: l=1, r=3, a=-10
  * best_prev = max(dp[0..1]) = max(0, 10) = 10
  * new_score = 10 + (-10) = 0
  * Update dp[2..4] = max(current, 0)
    - dp[2] = max(10, 0) = 10  (no change)
    - dp[3] = max(10, 0) = 10  (no change)
    - dp[4] = max(0, 0) = 0    (no change)
- Carry forward: dp[4] = max(dp[3], dp[4]) = max(10, 0) = 10
- State: [0, 10, 10, 10, 10, 0]

What does this mean?
- Query 2 has negative score, so we don't improve by activating it
- But we COULD place '1' at position 0 (dp[1]=10), skip positions 1-3,
  which avoids Query 2

Position 4 (Query 3 ends here: [2, 4] → +10):
- Query 3: l=2, r=4, a=10
  * best_prev = max(dp[0..2]) = max(0, 10, 10) = 10
  * new_score = 10 + 10 = 20
  * Update dp[3..5] = max(current, 20)
    - dp[3] = max(10, 20) = 20
    - dp[4] = max(10, 20) = 20
    - dp[5] = max(0, 20) = 20
- Carry forward: dp[5] = max(dp[4], dp[5]) = max(20, 20) = 20
- State: [0, 10, 10, 20, 20, 20]

What does this mean?
- dp[3]=20: Place '1' at positions 0 and 2 → activate Query 1 and Query 3
- dp[4]=20: Place '1' at positions 0 and 3 → activate Query 1 and Query 3
- dp[5]=20: Place '1' at positions 0 and 4 → activate Query 1 and Query 3

Final answer: max(dp) = 20 ✓

RECONSTRUCTION:
How do we get 20?
- dp[1] = 10 means: '1' at position 0 activates Query 1 → +10
- dp[5] = 20 means: Building on dp[1]=10, add '1' in [2,4] for Query 3 → +10
- Best choice: positions 0 and 4 → Total 20

WHY SEGMENT TREE HELPS:
- Without segment tree: O(n²) for range updates
- With segment tree: O(log n) per update
- With lazy propagation: Batch updates efficiently
- Total complexity: O(m log n) instead of O(mn²)
"""

def visualize_dp_evolution():
    print("=" * 70)
    print("DP ARRAY EVOLUTION")
    print("=" * 70)
    
    states = [
        ("Initial", [0, 0, 0, 0, 0, 0]),
        ("After pos 0", [0, 0, 0, 0, 0, 0]),
        ("After pos 1", [0, 0, 0, 0, 0, 0]),
        ("After pos 2 (Query 1: [0,2] +10)", [0, 10, 10, 10, 0, 0]),
        ("After pos 3 (Query 2: [1,3] -10)", [0, 10, 10, 10, 10, 0]),
        ("After pos 4 (Query 3: [2,4] +10)", [0, 10, 10, 20, 20, 20]),
    ]
    
    for label, state in states:
        print(f"\n{label}")
        print("Index: ", end="")
        for i in range(len(state)):
            print(f"{i:4}", end=" ")
        print()
        print("dp:    ", end="")
        for val in state:
            print(f"{val:4}", end=" ")
        print()
    
    print("\n" + "=" * 70)
    print("INTERPRETATION")
    print("=" * 70)
    print("\ndp[0] = 0:  No positions used → score 0")
    print("dp[1] = 10: Place '1' at pos 0 → Query 1 activated → score 10")
    print("dp[2] = 10: Place '1' at pos 1 → Query 1 activated → score 10")
    print("dp[3] = 20: Place '1' at pos 0 and 2 → Queries 1,3 → score 20")
    print("dp[4] = 20: Place '1' at pos 0 and 3 → Queries 1,3 → score 20")
    print("dp[5] = 20: Place '1' at pos 0 and 4 → Queries 1,3 → score 20")
    
    print("\nOptimal solution: dp[5] = 20")
    print("Configuration: '1' at positions 0 and 4")
    print("Binary string: 1 0 0 0 1")

if __name__ == "__main__":
    visualize_dp_evolution()
