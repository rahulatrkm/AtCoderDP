'''
Quick test to see which solution matches expected behavior
'''

from v import helper, helper_bottom_up

# Simple test case: 2 nodes connected 1-2
n = 2
edges = [(1, 2)]
m = 100

print("Test: 2 nodes (1-2)")
print(f"Your code:   {helper(n, edges, m)}")
print(f"Bottom-up:   {helper_bottom_up(n, edges, m)}")
print()

# What should it be?
# When node 1 is root: subtree at 2 has 1 node → (1+1)=2
# When node 2 is root: subtree at 1 has 1 node → (1+1)=2
# Expected: [2, 2]

print("Logical expectation: [2, 2]")
print()

# Another test: 3 nodes star 1-2, 1-3
n = 3
edges = [(1, 2), (1, 3)]
m = 100

print("Test: 3 nodes star (1-2, 1-3)")
print(f"Your code:   {helper(n, edges, m)}")
print(f"Bottom-up:   {helper_bottom_up(n, edges, m)}")
print()

# When node 1 is root: two subtrees (2 and 3), each size 1 → 2*2=4
# When node 2 is root: one subtree containing 1→3, size 2 → (1+2)=3
# When node 3 is root: one subtree containing 1→2, size 2 → (1+2)=3
# Expected: [4, 3, 3]

print("Logical expectation: [4, 3, 3]")
print()

print("=" * 60)
print("ANALYSIS:")
print("=" * 60)
print("Your code has a caching bug:")
print("  @lru_cache caches based on (node, col)")
print("  BUT 'vis' is a closure variable that changes between calls")
print("  This causes incorrect cache hits")
print()
print("If your code was ACCEPTED on AtCoder, it might be:")
print("  1. The test cases don't catch this bug, OR")
print("  2. The problem asks for something different")
print()
print("Bottom-up is the 'correct' mathematical interpretation")
print("of the tree DP problem.")
