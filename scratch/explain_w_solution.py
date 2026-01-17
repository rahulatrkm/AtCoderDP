"""
Problem W - Intervals: Step-by-step explanation

PROBLEM SETUP:
- You have n positions (0 to n-1) where you can place '1's or '0's
- m queries: each query (l, r, a) says:
  "If there's at least one '1' in positions [l, r], add 'a' to your score"
- Goal: Choose which positions get '1' to maximize total score

EXAMPLE:
n = 5 (positions 0,1,2,3,4)
Query 1: [0, 2] score +10  (if any '1' in positions 0,1,2 → add 10)
Query 2: [1, 3] score -10  (if any '1' in positions 1,2,3 → subtract 10)
Query 3: [2, 4] score +10  (if any '1' in positions 2,3,4 → add 10)

WHY GREEDY DOESN'T WORK:
Greedy: "Put '1' at position with most positive queries"
- Position 2 appears in all 3 queries
- If we place '1' at position 2: 10 - 10 + 10 = 10 points

But optimal solution:
- Place '1' at position 0: activates Query 1 (+10)
- Place '1' at position 4: activates Query 3 (+10)
- Skip position 2: avoids Query 2 (-10)
- Total: 20 points ✓

THE DP APPROACH:
Define: dp[i] = maximum score when considering positions 0..i

For each position i, we decide:
1. Place '0' at position i → dp[i] = dp[i-1] (carry forward)
2. Place '1' at position i → triggers all queries ending at or after i

KEY INSIGHT:
When we place a '1' at position i, which queries does it activate?
- All queries with l ≤ i ≤ r

OPTIMIZATION WITH SEGMENT TREE:
Process positions left to right. When we reach position i:
1. Check which queries have right endpoint = i
2. For each such query (l, r, a):
   - If we place '1' anywhere in [l, i], we get score 'a'
   - Best previous state: max(dp[0], dp[1], ..., dp[l])
   - Update: dp[l+1..i+1] can be at least (best_prev + a)

SEGMENT TREE OPERATIONS:
- Range Max Query: Find best previous score
- Range Add Update: Update all positions that benefit from this query
- Lazy Propagation: Efficiently handle range updates

WALKTHROUGH OF EXAMPLE:
Initial: dp = [0, 0, 0, 0, 0, 0]

Position 0:
- No queries end at position 0
- Carry forward: dp[1] = max(dp[1], dp[0]) = 0

Position 1:
- No queries end at position 1
- Carry forward: dp[2] = max(dp[2], dp[1]) = 0

Position 2:
- Query 1 ends here: [0, 2] score +10
  * If we place '1' at any position in [0, 2]:
  * Best previous: max(dp[0..0]) = 0
  * Update: dp[1..3] can be (0 + 10) = 10
  * New dp = [0, 10, 10, 10, 0, 0]
- Carry forward: dp[3] = max(dp[3], dp[2]) = 10

Position 3:
- Query 2 ends here: [1, 3] score -10
  * If we place '1' at any position in [1, 3]:
  * Best previous: max(dp[0..1]) = 10
  * Update: dp[2..4] can be (10 - 10) = 0
  * But current dp[2..4] = [10, 10, 0], so no update (max)
- Carry forward: dp[4] = max(dp[4], dp[3]) = 10

Position 4:
- Query 3 ends here: [2, 4] score +10
  * If we place '1' at any position in [2, 4]:
  * Best previous: max(dp[0..2]) = 10
  * Update: dp[3..5] can be (10 + 10) = 20
  * New dp = [0, 10, 10, 20, 20, 20]
- Carry forward: dp[5] = max(dp[5], dp[4]) = 20

Answer: max(dp) = 20 ✓

WHY THIS WORKS:
- We consider every possible placement of '1's
- For each query, we track the best score if we activate it
- Segment tree efficiently handles overlapping ranges
- Time: O(m * log n) per query, total O(m log n)

COMPARISON:
Greedy approach: Places '1's based on local decisions → Wrong
DP approach: Considers all valid configurations → Correct
"""

def explain_example():
    print("=" * 60)
    print("EXAMPLE WALKTHROUGH")
    print("=" * 60)
    
    print("\nInput:")
    print("n = 5 positions")
    print("Query 1: [0, 2] → +10")
    print("Query 2: [1, 3] → -10")
    print("Query 3: [2, 4] → +10")
    
    print("\n" + "=" * 60)
    print("GREEDY APPROACH (WRONG)")
    print("=" * 60)
    print("\nPosition 2 appears in all 3 queries (most coverage)")
    print("Place '1' at position 2:")
    print("  ✓ Activates Query 1: +10")
    print("  ✓ Activates Query 2: -10")
    print("  ✓ Activates Query 3: +10")
    print("Total: 10 - 10 + 10 = 10 points")
    
    print("\n" + "=" * 60)
    print("DP APPROACH (CORRECT)")
    print("=" * 60)
    print("\nOptimal placement:")
    print("String: 1 0 0 0 1")
    print("        ↑       ↑")
    print("        |       └─ position 4")
    print("        └─ position 0")
    print("\nActivated queries:")
    print("  ✓ Query 1 [0,2]: position 0 has '1' → +10")
    print("  ✗ Query 2 [1,3]: no '1' in range → 0")
    print("  ✓ Query 3 [2,4]: position 4 has '1' → +10")
    print("Total: 10 + 0 + 10 = 20 points ✓")
    
    print("\n" + "=" * 60)
    print("KEY INSIGHT")
    print("=" * 60)
    print("\nOne '1' can activate MULTIPLE queries")
    print("But we want to AVOID queries with negative scores!")
    print("\nDP lets us consider:")
    print("- Which queries to activate")
    print("- Which queries to skip")
    print("- Optimal placement for maximum score")

if __name__ == "__main__":
    explain_example()
