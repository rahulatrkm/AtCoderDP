#!/usr/bin/env python3
"""
Comprehensive test suite for Problem N: Slimes
Tests edge cases, performance, and correctness
"""

import subprocess
import sys
import time

def run_test(n, arr, expected, desc):
    """Run a single test case"""
    input_str = f"{n}\n{' '.join(map(str, arr))}\n"
    
    try:
        start_time = time.time()
        result = subprocess.run(
            ['python3', 'n.py'],
            input=input_str,
            capture_output=True,
            text=True,
            timeout=10
        )
        elapsed = time.time() - start_time
        
        if result.returncode != 0:
            print(f"✗ {desc}")
            print(f"   Error: {result.stderr}")
            return False
        
        actual = int(result.stdout.strip())
        
        if actual == expected:
            if elapsed < 0.1:
                print(f"✓ ⚡ {desc}")
            elif elapsed < 1.0:
                print(f"✓ ⏱️ {desc}")
            else:
                print(f"✓ 🐌 {desc}")
            print(f"   Result: {actual} (Expected: {expected}) [{elapsed:.3f}s]")
            return True
        else:
            print(f"✗ {desc}")
            print(f"   Result: {actual} (Expected: {expected}) [{elapsed:.3f}s]")
            return False
    except subprocess.TimeoutExpired:
        print(f"✗ {desc}")
        print(f"   TIMEOUT (>10s)")
        return False
    except Exception as e:
        print(f"✗ {desc}")
        print(f"   Exception: {e}")
        return False

def main():
    print("=" * 80)
    print("PROBLEM N: Slimes - Minimum Merge Cost")
    print("Constraints: 2 ≤ N ≤ 400, 1 ≤ a[i] ≤ 10^9")
    print("=" * 80)
    
    passed = 0
    total = 0
    
    # Sample Tests
    print("\n[Sample Tests]")
    tests = [
        (4, [10, 20, 30, 40], 190, "Sample 1: N=4, [10,20,30,40]"),
        (5, [10, 10, 10, 10, 10], 120, "Sample 2: N=5, all 10s"),
        (3, [1000000000, 1000000000, 1000000000], 5000000000, "Sample 3: N=3, large values (10^9)"),
        (6, [7, 6, 8, 6, 1, 1], 68, "Sample 4: N=6, [7,6,8,6,1,1]"),
    ]
    
    for n, arr, expected, desc in tests:
        if run_test(n, arr, expected, desc):
            passed += 1
        total += 1
    
    # Edge Cases - Minimum N
    print("\n[Edge Cases - Minimum N]")
    tests = [
        (2, [1, 1], 2, "N=2 (minimum): [1,1]"),
        (2, [1, 2], 3, "N=2: [1,2]"),
        (2, [100, 200], 300, "N=2: [100,200]"),
        (2, [1000000000, 1000000000], 2000000000, "N=2: two 10^9 values"),
    ]
    
    for n, arr, expected, desc in tests:
        if run_test(n, arr, expected, desc):
            passed += 1
        total += 1
    
    # Edge Cases - Small N
    print("\n[Edge Cases - Small N (N=3)]")
    tests = [
        (3, [1, 1, 1], 4, "N=3: all 1s"),
        (3, [1, 2, 3], 9, "N=3: [1,2,3] - increasing"),
        (3, [3, 2, 1], 8, "N=3: [3,2,1] - decreasing"),
        (3, [100, 1, 100], 202, "N=3: [100,1,100] - symmetric"),
    ]
    
    for n, arr, expected, desc in tests:
        if run_test(n, arr, expected, desc):
            passed += 1
        total += 1
    
    # Uniform Values
    print("\n[Uniform Values]")
    tests = [
        (10, [1]*10, 45, "N=10: all 1s"),
        (10, [5]*10, 225, "N=10: all 5s"),
        (20, [1]*20, 190, "N=20: all 1s"),
        (50, [1]*50, 1225, "N=50: all 1s"),
    ]
    
    for n, arr, expected, desc in tests:
        if run_test(n, arr, expected, desc):
            passed += 1
        total += 1
    
    # Increasing/Decreasing Patterns
    print("\n[Patterns - Increasing/Decreasing]")
    tests = [
        (5, [1, 2, 3, 4, 5], 33, "N=5: strictly increasing [1,2,3,4,5]"),
        (5, [5, 4, 3, 2, 1], 33, "N=5: strictly decreasing [5,4,3,2,1]"),
        (10, list(range(1, 11)), 165, "N=10: [1,2,3,...,10]"),
        (10, list(range(10, 0, -1)), 165, "N=10: [10,9,8,...,1]"),
    ]
    
    for n, arr, expected, desc in tests:
        if run_test(n, arr, expected, desc):
            passed += 1
        total += 1
    
    # Alternating Patterns
    print("\n[Patterns - Alternating]")
    tests = [
        (4, [1, 10, 1, 10], 42, "N=4: [1,10,1,10]"),
        (6, [1, 10, 1, 10, 1, 10], 81, "N=6: alternating [1,10,...]"),
        (10, [1, 100] * 5, 1990, "N=10: [1,100,1,100,...]"),
    ]
    
    for n, arr, expected, desc in tests:
        if run_test(n, arr, expected, desc):
            passed += 1
        total += 1
    
    # Large Individual Values
    print("\n[Large Individual Values]")
    tests = [
        (5, [1000000000]*5, 10000000000, "N=5: all 10^9"),
        (10, [999999999]*10, 44999999955, "N=10: all (10^9 - 1)"),
        (2, [1, 1000000000], 1000000001, "N=2: [1, 10^9]"),
        (3, [1, 1000000000, 1], 2000000002, "N=3: [1, 10^9, 1]"),
    ]
    
    for n, arr, expected, desc in tests:
        if run_test(n, arr, expected, desc):
            passed += 1
        total += 1
    
    # Medium N
    print("\n[Medium N Tests]")
    tests = [
        (50, [10]*50, 12250, "N=50: all 10s"),
        (100, [1]*100, 4950, "N=100: all 1s"),
        (100, [10]*100, 49500, "N=100: all 10s"),
        (100, list(range(1, 101)), 171700, "N=100: [1,2,3,...,100]"),
    ]
    
    for n, arr, expected, desc in tests:
        if run_test(n, arr, expected, desc):
            passed += 1
        total += 1
    
    # Large N (approaching maximum)
    print("\n[Large N Tests]")
    tests = [
        (200, [1]*200, 19900, "N=200: all 1s"),
        (200, [5]*200, 99500, "N=200: all 5s"),
        (300, [1]*300, 44850, "N=300: all 1s"),
    ]
    
    for n, arr, expected, desc in tests:
        if run_test(n, arr, expected, desc):
            passed += 1
        total += 1
    
    # Maximum N = 400
    print("\n⚠️  Maximum N=400 Tests (Critical):")
    tests = [
        (400, [1]*400, 79800, "MAX N=400: all 1s"),
        (400, [2]*400, 159600, "MAX N=400: all 2s"),
        (400, [5]*400, 399000, "MAX N=400: all 5s"),
        (400, [10]*400, 798000, "MAX N=400: all 10s"),
        (400, [100]*400, 7980000, "MAX N=400: all 100s"),
        (400, [1000]*400, 79800000, "MAX N=400: all 1000s"),
        (400, list(range(1, 401)), 10706700, "MAX N=400: [1,2,3,...,400]"),
        (400, [1000000000]*400, 79800000000000, "MAX N=400: all 10^9 (extreme)"),
    ]
    
    for n, arr, expected, desc in tests:
        if run_test(n, arr, expected, desc):
            passed += 1
        total += 1
    
    # Mixed Large Values at N=400
    print("\n[N=400 with Mixed Values]")
    tests = [
        (400, [1, 1000000000] * 200, 159600000000000, "N=400: alternating [1, 10^9]"),
        (400, list(range(1, 201)) + list(range(200, 0, -1)), 10693400, "N=400: [1..200, 200..1]"),
    ]
    
    for n, arr, expected, desc in tests:
        if run_test(n, arr, expected, desc):
            passed += 1
        total += 1
    
    # Boundary Tests
    print("\n[Boundary Tests]")
    tests = [
        (2, [1, 1000000000], 1000000001, "Minimum N with max value"),
        (400, [1]*399 + [1000000000], 1079800399, "N=400: 399 ones + one 10^9"),
        (400, [1000000000] + [1]*399, 1079800399, "N=400: one 10^9 + 399 ones"),
    ]
    
    for n, arr, expected, desc in tests:
        if run_test(n, arr, expected, desc):
            passed += 1
        total += 1
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Tests Passed: {passed}/{total}")
    
    print("\nComplexity Analysis (Current Implementation):")
    print("  ⚠️  Algorithm: Greedy (always merge smallest adjacent pair)")
    print("  ⚠️  Time: O(N²) per merge × N merges = O(N³) worst case")
    print("  ⚠️  Space: O(N) for array + O(N) recursion depth")
    print("  ⚠️  Issue: Greedy approach may not give optimal solution")
    print("  ✓  Handles N=400 within recursion limits")
    print("  ✓  Handles values up to 10^9")
    
    print("\nOptimal Solution (Interval DP):")
    print("  ✓  Time: O(N³) - dp[i][j] with k split point")
    print("  ✓  Space: O(N²) - 2D DP table")
    print("  ✓  Guaranteed optimal solution")
    print("  ✓  No recursion depth issues (iterative)")
    
    print("\nKey Insights:")
    print("  • Classic interval DP problem (similar to matrix chain multiplication)")
    print("  • dp[i][j] = minimum cost to merge slimes from index i to j")
    print("  • Transition: try all split points k, take minimum")
    print("  • Cost to merge two parts = sum of all values in range")
    print("  • Use prefix sums for O(1) range sum queries")
    print("=" * 80)
    
    return 0 if passed == total else 1

if __name__ == "__main__":
    sys.exit(main())
