"""
Why Simple DP Fails - Detailed Explanation

The failing test case:
n=3, queries: [0,2]+100, [0,0]-10, [1,1]-20, [2,2]-30
Expected: 90 (place '1' at position 0: Query 0 and 1 activate)
"""

from collections import defaultdict

print("=" * 70)
print("TRACING SIMPLE DP (BUGGY)")
print("=" * 70)
print()

by_right = defaultdict(list)
for l, r, a in [(0, 2, 100), (0, 0, -10), (1, 1, -20), (2, 2, -30)]:
    by_right[r].append((l, a))

dp = [0, 0, 0, 0]
print(f"Initial: dp = {dp}\n")

for i in range(3):
    print(f"=== Position {i} ===")
    
    if i in by_right:
        old_dp = dp[:]  # Save state before updates
        for l, a in by_right[i]:
            print(f"Query [{l}, {i}] → {a:+d}")
            prev_best = max(old_dp[0:l]) if l > 0 else 0
            print(f"  prev_best = max(old_dp[0:{l}]) = {prev_best}")
            new_val = prev_best + a
            print(f"  new_val = {new_val}")
            
            for j in range(l + 1, i + 2):
                old = dp[j]
                dp[j] = max(dp[j], new_val)  # ← THE BUG IS HERE
                if old != dp[j]:
                    print(f"  dp[{j}]: {old} → {dp[j]}")
    
    if i + 1 <= 3:
        dp[i+1] = max(dp[i+1], dp[i])
    
    print(f"After: dp = {dp}\n")

print(f"Result: {dp[3]}")
print()

print("=" * 70)
print("THE PROBLEM")
print("=" * 70)
print()
print("At position 2, two queries end:")
print()
print("1. Query [0,2] → +100")
print("   - prev_best = 0")
print("   - new_val = 100")
print("   - Updates: dp[1]=100, dp[2]=100, dp[3]=100")
print()
print("2. Query [2,2] → -30")
print("   - prev_best = max(old_dp[0:2]) = max([0, 0]) = 0")
print("   - new_val = 0 + (-30) = -30")
print("   - Tries to update dp[3] = max(100, -30) = 100")
print()
print("LOOKS CORRECT, RIGHT? But it's not!")
print()
print("The issue: dp[1] and dp[2] weren't updated yet when we saved old_dp.")
print("So prev_best for Query [2,2] reads from BEFORE Query [0,2] processed.")
print()
print("But then we do: dp[3] = max(100, -30) = 100")
print("         This ↑ 100 came from Query [0,2]!")
print()
print("We're saying: 'keep 100 from Query [0,2] instead of -30 from Query [2,2]'")
print("But this is WRONG because:")
print()
print("dp[3] = 100 means: 'place 1 somewhere in [0,2] → get +100'")
print()
print("This implicitly places '1' at position 0, 1, or 2.")
print("If position 2 has '1', Query [2,2] MUST activate!")
print("We can't have +100 without -30 if '1' is at position 2!")
print()

print("=" * 70)
print("THE FUNDAMENTAL ISSUE")
print("=" * 70)
print()
print("Simple DP with max(dp[j], new_val) treats each query independently.")
print()
print("Query [0,2]: 'You can get 100 by placing 1 in [0,2]'")
print("Query [2,2]: 'You can get -30 by placing 1 at [2]'")
print()
print("max(100, -30) = 100 says: 'Choose the first option'")
print()
print("But if you place '1' at position 2:")
print("  - It's in range [0,2] → Query [0,2] activates → +100")
print("  - It's in range [2,2] → Query [2,2] activates → -30")
print("  - Total: 100 + (-30) = 70, not 100!")
print()
print("The max() operation doesn't know that the '100' option")
print("might OVERLAP with the '-30' option!")
print()

print("=" * 70)
print("WHY LAZY SEGMENT TREE WORKS")
print("=" * 70)
print()
print("Line 82 in w_correct.py:")
print("st.update(1, 0, n, l+1, i+1, new_val - st.query(1, 0, n, l+1, l+1))")
print()
print("This does: dp[l+1..i+1] += (new_val - current_value)")
print()
print("If current_value = 100 and new_val = 70:")
print("  Update by (70 - 100) = -30")
print("  New value: 100 + (-30) = 70")
print()
print("This REPLACES the value, not max() with it!")
print()
print("Combined with how the segment tree processes updates,")
print("it ensures that overlapping queries are handled correctly.")
print("The tree structure maintains max across different branches,")
print("preventing the double-counting issue.")
print()

print("=" * 70)
print("CORRECT ANSWER")
print("=" * 70)
print()
print("Configuration '100' (position 0 only):")
print("  - Query [0,2]: position 0 is in range → +100")
print("  - Query [0,0]: position 0 is in range → -10")
print("  - Query [1,1]: position 0 NOT in range → 0")
print("  - Query [2,2]: position 0 NOT in range → 0")
print("  Total: 100 - 10 = 90 ✓")
