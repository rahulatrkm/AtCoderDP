'''
Test the tabular solution
'''

from v import helper, helper_bottom_up, helper_tabular

test_cases = [
    (1, [], 100, "Single node"),
    (2, [(1, 2)], 100, "2 nodes"),
    (3, [(1, 2), (1, 3)], 100, "3 nodes star"),
    (5, [(1, 2), (2, 3), (3, 4), (4, 5)], 1000, "5 nodes linear"),
    (5, [(1, 2), (1, 3), (1, 4), (1, 5)], 1000, "5 nodes star"),
    (7, [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)], 10000, "Complete binary"),
    (5, [(1, 2), (2, 3), (3, 4), (4, 5)], 1, "M=1 edge case"),
]

print("=" * 80)
print("TESTING TABULAR SOLUTION")
print("=" * 80)

all_match = True

for n, edges, m, desc in test_cases:
    result_original = helper(n, edges, m)
    result_bottom_up = helper_bottom_up(n, edges, m)
    result_tabular = helper_tabular(n, edges, m)
    
    match = (result_tabular == result_bottom_up)
    status = "✓" if match else "✗"
    
    print(f"\n{desc} (n={n}, m={m}):")
    print(f"  Original:   {result_original}")
    print(f"  Bottom-up:  {result_bottom_up}")
    print(f"  Tabular:    {result_tabular}")
    print(f"  {status} {'MATCH' if match else 'DIFFER'}")
    
    if not match:
        all_match = False

print("\n" + "=" * 80)
if all_match:
    print("✓ SUCCESS! Tabular solution matches bottom-up (correct)")
else:
    print("✗ Tabular solution differs from bottom-up")
print("=" * 80)

print("\nSOLUTION COMPARISON:")
print("-" * 80)
print("1. helper (original):")
print("   • Recursive with @lru_cache memoization")
print("   • Uses vis set + parent parameter")
print("   • Space: O(N²) from cache")
print()
print("2. helper_bottom_up:")
print("   • Recursive DFS without memoization")
print("   • Clean and simple")
print("   • Space: O(N) from recursion stack")
print()
print("3. helper_tabular (NEW):")
print("   • Iterative with explicit stack (no recursion)")
print("   • Uses DP table for results")
print("   • Space: O(N) from stack + DP table")
print("   • More 'traditional' DP style")
print("=" * 80)
