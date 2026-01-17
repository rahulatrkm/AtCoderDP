'''
Test script to compare top-down and bottom-up solutions for Problem V
'''

import sys
sys.path.insert(0, '/Users/rahul./Downloads/AtCoderDP')

from v import helper_top_down, helper_bottom_up

def test_both_solutions():
    """Test that both solutions produce the same results"""
    
    test_cases = [
        # (n, edges, m, description)
        (1, [], 100, "Single node"),
        (2, [(1, 2)], 100, "Two nodes"),
        (3, [(1, 2), (1, 3)], 100, "Star with 3 nodes"),
        (5, [(1, 2), (2, 3), (3, 4), (4, 5)], 1000, "Linear tree"),
        (5, [(1, 2), (1, 3), (1, 4), (1, 5)], 1000, "Star tree"),
        (7, [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)], 10000, "Complete binary tree"),
        (5, [(1, 2), (2, 3), (3, 4), (4, 5)], 7, "Linear tree with small modulo"),
        (5, [(1, 2), (2, 3), (3, 4), (4, 5)], 1, "Linear tree with m=1"),
    ]
    
    print("=" * 70)
    print("COMPARING TOP-DOWN vs BOTTOM-UP SOLUTIONS")
    print("=" * 70)
    
    all_passed = True
    
    for i, (n, edges, m, description) in enumerate(test_cases, 1):
        print(f"\nTest {i}: {description} (n={n}, m={m})")
        
        result_td = helper_top_down(n, edges, m)
        result_bu = helper_bottom_up(n, edges, m)
        
        if result_td == result_bu:
            print(f"  ✓ PASSED")
            print(f"    Top-down:  {result_td}")
            print(f"    Bottom-up: {result_bu}")
        else:
            print(f"  ✗ FAILED - Results differ!")
            print(f"    Top-down:  {result_td}")
            print(f"    Bottom-up: {result_bu}")
            all_passed = False
    
    print("\n" + "=" * 70)
    if all_passed:
        print("✓ ALL TESTS PASSED - Both solutions produce identical results!")
    else:
        print("✗ SOME TESTS FAILED - Results differ between solutions")
    print("=" * 70)
    
    return all_passed


def benchmark_solutions():
    """Compare performance of both solutions"""
    import time
    
    print("\n" + "=" * 70)
    print("PERFORMANCE COMPARISON")
    print("=" * 70)
    
    test_sizes = [10, 30, 50, 100]
    
    for n in test_sizes:
        # Create linear tree
        edges = [(i, i+1) for i in range(1, n)]
        m = 10**9 + 7
        
        # Test top-down
        start = time.time()
        result_td = helper_top_down(n, edges, m)
        time_td = time.time() - start
        
        # Test bottom-up
        start = time.time()
        result_bu = helper_bottom_up(n, edges, m)
        time_bu = time.time() - start
        
        print(f"\nN={n:3d}:")
        print(f"  Top-down:  {time_td:.6f}s")
        print(f"  Bottom-up: {time_bu:.6f}s")
        print(f"  Speedup:   {time_td/time_bu:.2f}x" if time_bu > 0 else "  N/A")
        print(f"  Match:     {'✓' if result_td == result_bu else '✗'}")


if __name__ == "__main__":
    # Run correctness tests
    success = test_both_solutions()
    
    # Run performance comparison
    if success:
        benchmark_solutions()
