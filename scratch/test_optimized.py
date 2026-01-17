'''
Test the optimized O(N) rerooting solution
'''

from v import helper, helper_bottom_up, helper_optimized
import time

print("=" * 80)
print("TESTING OPTIMIZED O(N) REROOTING SOLUTION")
print("=" * 80)

# Correctness tests
test_cases = [
    (1, [], 100, "Single node"),
    (2, [(1, 2)], 100, "2 nodes"),
    (3, [(1, 2), (1, 3)], 100, "3 nodes star"),
    (5, [(1, 2), (2, 3), (3, 4), (4, 5)], 1000, "5 nodes linear"),
    (5, [(1, 2), (1, 3), (1, 4), (1, 5)], 1000, "5 nodes star"),
    (7, [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)], 10000, "Complete binary"),
    (10, [(i, i+1) for i in range(1, 10)], 7, "Linear N=10"),
]

print("\n" + "=" * 80)
print("CORRECTNESS TESTS")
print("=" * 80)

all_match = True

for n, edges, m, desc in test_cases:
    result_correct = helper_bottom_up(n, edges, m)
    result_optimized = helper_optimized(n, edges, m)
    
    match = result_optimized == result_correct
    status = "✓" if match else "✗"
    
    print(f"\n{desc} (n={n}, m={m}): {status}")
    if not match or n <= 5:
        print(f"  Expected:  {result_correct}")
        print(f"  Optimized: {result_optimized}")
    
    if not match:
        all_match = False
        print(f"  ✗ MISMATCH!")

print("\n" + "=" * 80)
if all_match:
    print("✓ ALL CORRECTNESS TESTS PASSED!")
else:
    print("✗ Some tests failed - need to fix")
print("=" * 80)

if all_match:
    print("\n" + "=" * 80)
    print("PERFORMANCE COMPARISON: O(N²) vs O(N)")
    print("=" * 80)
    
    test_sizes = [10, 50, 100, 500, 1000]
    
    for n in test_sizes:
        # Create linear tree
        edges = [(i, i+1) for i in range(1, n)]
        m = 10**9 + 7
        
        # Test O(N²) solution
        start = time.time()
        result_n2 = helper_bottom_up(n, edges, m)
        time_n2 = time.time() - start
        
        # Test O(N) solution
        start = time.time()
        result_n = helper_optimized(n, edges, m)
        time_n = time.time() - start
        
        match = result_n2 == result_n
        speedup = time_n2 / time_n if time_n > 0 else 0
        
        print(f"\nN = {n:4d}:")
        print(f"  O(N²) Bottom-up:  {time_n2:.6f}s")
        print(f"  O(N) Optimized:   {time_n:.6f}s")
        print(f"  Speedup:          {speedup:.2f}x {'✓' if match else '✗'}")
    
    print("\n" + "=" * 80)
    print("COMPLEXITY COMPARISON")
    print("=" * 80)
    print("Original solutions:  O(N²) time, O(N) or O(N²) space")
    print("Optimized solution:  O(N) time,  O(N) space")
    print()
    print("The optimization uses REROOTING DP:")
    print("  1. Compute subtree products from one root: O(N)")
    print("  2. Reroot dynamically to all nodes: O(N)")
    print("  Total: O(N) instead of O(N²)!")
    print()
    print("This is a HUGE improvement for large trees!")
    print("=" * 80)
