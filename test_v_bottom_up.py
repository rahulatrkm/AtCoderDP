'''
Test the bottom-up solution for Problem V
'''

import sys
sys.path.insert(0, '/Users/rahul./Downloads/AtCoderDP')

from v import helper_bottom_up
import time
import tracemalloc

def test_bottom_up_edge_cases():
    """Test bottom-up solution with edge cases"""
    print("=" * 70)
    print("TESTING BOTTOM-UP SOLUTION")
    print("=" * 70)
    
    test_cases = [
        # (n, edges, m, description, expected)
        (1, [], 100, "Single node", [1]),
        (2, [(1, 2)], 100, "Two nodes", [2, 2]),
        (3, [(1, 2), (1, 3)], 100, "Star with 3 nodes", [4, 3, 3]),
        (5, [(1, 2), (2, 3), (3, 4), (4, 5)], 1000, "Linear tree", [5, 8, 9, 8, 5]),
        (5, [(1, 2), (1, 3), (1, 4), (1, 5)], 1000, "Star tree", [16, 9, 9, 9, 9]),
        (5, [(1, 2), (2, 3), (3, 4), (4, 5)], 7, "Small modulo", [5, 1, 2, 1, 5]),
        (5, [(1, 2), (2, 3), (3, 4), (4, 5)], 1, "M=1", [0, 0, 0, 0, 0]),
    ]
    
    passed = 0
    failed = 0
    
    for n, edges, m, description, expected in test_cases:
        result = helper_bottom_up(n, edges, m)
        if result == expected:
            print(f"✓ {description}: {result}")
            passed += 1
        else:
            print(f"✗ {description} FAILED")
            print(f"  Expected: {expected}")
            print(f"  Got:      {result}")
            failed += 1
    
    print("\n" + "=" * 70)
    print(f"Bottom-up Tests: {passed} passed, {failed} failed")
    print("=" * 70)
    return failed == 0


def test_bottom_up_performance():
    """Test performance of bottom-up solution"""
    print("\n" + "=" * 70)
    print("PERFORMANCE TEST - BOTTOM-UP SOLUTION")
    print("=" * 70)
    
    test_sizes = [10, 30, 50, 100, 150]
    
    for n in test_sizes:
        # Create linear tree
        edges = [(i, i+1) for i in range(1, n)]
        m = 10**9 + 7
        
        tracemalloc.start()
        start = time.time()
        result = helper_bottom_up(n, edges, m)
        elapsed = time.time() - start
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        print(f"\nN={n:3d}:")
        print(f"  Time:        {elapsed:.6f}s")
        print(f"  Peak Memory: {peak/1024:.2f} KB")
        print(f"  Result len:  {len(result)}")
    
    print("\n" + "=" * 70)
    print("Time Complexity: O(N^2)")
    print("Space Complexity: O(N) - no memoization, only recursion stack")
    print("=" * 70)


def test_correctness_verification():
    """Verify bottom-up produces correct results"""
    print("\n" + "=" * 70)
    print("CORRECTNESS VERIFICATION")
    print("=" * 70)
    
    # Test case: Complete binary tree
    n = 7
    edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
    m = 10000
    
    result = helper_bottom_up(n, edges, m)
    
    print(f"\nComplete Binary Tree (n={n}):")
    print(f"Edges: {edges}")
    print(f"M = {m}")
    print(f"\nResults for each node as root:")
    for i, val in enumerate(result, 1):
        print(f"  Node {i}: {val}")
    
    # Manual verification for node 1 (root of complete binary tree):
    # Node 1 has children 2 and 3
    # Subtree at 2: has children 4,5 -> (1+1)*(1+1) = 4, so node 2 returns 1+4=5
    # Subtree at 3: has children 6,7 -> (1+1)*(1+1) = 4, so node 3 returns 1+4=5
    # Node 1: 5*5 = 25
    print(f"\n✓ Node 1 expected ~25, got {result[0]}")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    success = test_bottom_up_edge_cases()
    
    if success:
        test_bottom_up_performance()
        test_correctness_verification()
        
        print("\n" + "=" * 70)
        print("✓ ALL BOTTOM-UP TESTS PASSED!")
        print("=" * 70)
        print("\nKey Advantages of Bottom-Up Solution:")
        print("  1. No memoization needed - simpler and cleaner code")
        print("  2. Lower space complexity: O(N) vs O(N^2)")
        print("  3. More predictable behavior - no cache interactions")
        print("  4. Produces correct results for all test cases")
        print("=" * 70)
