#!/usr/bin/env python3
"""
Comprehensive test suite for Problem M: Candies
https://atcoder.jp/contests/dp/tasks/dp_m

Problem: Distribute K candies among N children.
Child i can receive at most a[i] candies.
Count ways modulo 10^9+7.

Constraints:
- 1 ≤ N ≤ 100
- 0 ≤ K ≤ 10^5
- 0 ≤ a[i] ≤ K

Expected Complexity:
- Time: O(N × K) with prefix sum optimization
- Space: O(N × K) for DP table
"""

import subprocess
import time
import sys

def run_test(n, k, arr, expected, description):
    """Run a single test case"""
    input_data = f"{n} {k}\n{' '.join(map(str, arr))}\n"
    
    try:
        start = time.time()
        result = subprocess.run(
            ['python3', 'm.py'],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=10
        )
        elapsed = time.time() - start
        
        if result.returncode != 0:
            print(f"✗ {description}: CRASHED")
            print(f"   Error: {result.stderr[:200]}")
            return False
        
        output = result.stdout.strip()
        
        try:
            result_val = int(output)
            if result_val == expected:
                speed = "⚡" if elapsed < 0.1 else "⏱️" if elapsed < 1.0 else "🐌"
                print(f"✓ {speed} {description}")
                print(f"   Result: {result_val} (Expected: {expected}) [{elapsed:.3f}s]")
                return True
            else:
                print(f"✗ {description}")
                print(f"   Result: {result_val} (Expected: {expected}) [{elapsed:.3f}s]")
                return False
        except ValueError:
            print(f"✗ {description}: Invalid output '{output}'")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"✗ {description}: TIMEOUT (>10s)")
        return False
    except Exception as e:
        print(f"✗ {description}: ERROR - {str(e)}")
        return False

def main():
    print("=" * 80)
    print("PROBLEM M: Candies - Distribution Counting")
    print("Constraints: N ≤ 100, K ≤ 10^5, 0 ≤ a[i] ≤ K")
    print("=" * 80)
    
    passed = 0
    total = 0
    
    # Sample Tests
    print("\n[Sample Tests]")
    tests = [
        (3, 4, [1, 2, 3], 5, "Sample 1: N=3, K=4, [1,2,3]"),
        (2, 3, [2, 2], 2, "Sample 2: N=2, K=3, [2,2]"),
        (1, 9, [9], 1, "Sample 3: N=1, K=9, [9]"),
        (2, 0, [0, 0], 1, "Sample 4: N=2, K=0 (give 0 to both)"),
    ]
    
    for n, k, arr, expected, desc in tests:
        if run_test(n, k, arr, expected, desc):
            passed += 1
        total += 1
    
    # Edge Cases - K=0
    print("\n[Edge Cases - K=0]")
    tests = [
        (1, 0, [0], 1, "K=0: 1 child, can't give any"),
        (1, 0, [5], 1, "K=0: 1 child with a[0]=5, give 0"),
        (3, 0, [1, 2, 3], 1, "K=0: 3 children, give 0 to all"),
        (5, 0, [0, 0, 0, 0, 0], 1, "K=0: 5 children, all limits 0"),
    ]
    
    for n, k, arr, expected, desc in tests:
        if run_test(n, k, arr, expected, desc):
            passed += 1
        total += 1
    
    # Edge Cases - Single Child
    print("\n[Edge Cases - Single Child]")
    tests = [
        (1, 1, [1], 1, "N=1, K=1, a[0]=1"),
        (1, 5, [5], 1, "N=1, K=5, a[0]=5"),
        (1, 5, [3], 0, "N=1, K=5, a[0]=3 (impossible)"),
        (1, 10, [20], 1, "N=1, K=10, a[0]=20 (enough capacity)"),
        (1, 100, [100], 1, "N=1, K=100, a[0]=100"),
    ]
    
    for n, k, arr, expected, desc in tests:
        if run_test(n, k, arr, expected, desc):
            passed += 1
        total += 1
    
    # Edge Cases - All zeros
    print("\n[Edge Cases - All Zeros]")
    tests = [
        (2, 1, [0, 0], 0, "N=2, K=1, all limits 0 (impossible)"),
        (3, 5, [0, 0, 0], 0, "N=3, K=5, all limits 0"),
        (2, 0, [0, 0], 1, "N=2, K=0, all limits 0 (valid)"),
    ]
    
    for n, k, arr, expected, desc in tests:
        if run_test(n, k, arr, expected, desc):
            passed += 1
        total += 1
    
    # Small K
    print("\n[Small K Values]")
    tests = [
        (2, 1, [1, 1], 2, "N=2, K=1, [1,1]: (0,1) or (1,0)"),
        (3, 2, [1, 1, 1], 3, "N=3, K=2, [1,1,1]: choose 2 from 3"),
        (2, 2, [1, 1], 1, "N=2, K=2, [1,1]: (1,1) only"),
        (2, 2, [2, 2], 3, "N=2, K=2, [2,2]: (0,2),(1,1),(2,0)"),
        (4, 3, [1, 1, 1, 1], 4, "N=4, K=3, all 1s: choose 3 from 4"),
    ]
    
    for n, k, arr, expected, desc in tests:
        if run_test(n, k, arr, expected, desc):
            passed += 1
        total += 1
    
    # Symmetric Cases
    print("\n[Symmetric Cases]")
    tests = [
        (2, 5, [5, 5], 6, "N=2, K=5, [5,5]: symmetric"),
        (3, 3, [3, 3, 3], 10, "N=3, K=3, all 3s"),
        (4, 2, [2, 2, 2, 2], 10, "N=4, K=2, all 2s"),
    ]
    
    for n, k, arr, expected, desc in tests:
        if run_test(n, k, arr, expected, desc):
            passed += 1
        total += 1
    
    # Large Individual Limits
    print("\n[Large Individual Limits]")
    tests = [
        (2, 10, [100, 100], 11, "Large limits: essentially choose K+1 ways"),
        (3, 5, [100, 100, 100], 21, "N=3, K=5, unlimited: C(5+3-1,3-1)=C(7,2)=21"),
        (2, 100, [100, 100], 101, "N=2, K=100, [100,100]"),
    ]
    
    for n, k, arr, expected, desc in tests:
        if run_test(n, k, arr, expected, desc):
            passed += 1
        total += 1
    
    # Varied Limits
    print("\n[Varied Limits]")
    tests = [
        (3, 5, [1, 2, 5], 6, "N=3, K=5, [1,2,5]"),
        (4, 6, [1, 2, 3, 4], 20, "N=4, K=6, [1,2,3,4]"),
        (5, 10, [2, 2, 2, 2, 2], 1, "N=5, K=10, all 2s (only way: 2 each)"),
    ]
    
    for n, k, arr, expected, desc in tests:
        if run_test(n, k, arr, expected, desc):
            passed += 1
        total += 1
    
    # Medium Size
    print("\n[Medium Size Tests]")
    tests = [
        (10, 10, [1]*10, 1, "N=10, K=10, all 1s"),
        (10, 20, [2]*10, 1, "N=10, K=20, all 2s (K=sum, only 1 way)"),
        (20, 50, [5]*20, 974573304, "N=20, K=50, all 5s (with mod)"),
    ]
    
    for n, k, arr, expected, desc in tests:
        if run_test(n, k, arr, expected, desc):
            passed += 1
        total += 1
    
    # Large K
    print("\n[Large K Tests]")
    tests = [
        (2, 1000, [1000, 1000], 1001, "N=2, K=1000"),
        (3, 1000, [500, 500, 500], 125751, "N=3, K=1000, [500,500,500]"),
        (5, 5000, [1000]*5, 1, "N=5, K=5000, all 1000s (K=sum, only 1 way)"),
        (10, 10000, [1000]*10, 1, "N=10, K=10000, all 1000s (K=sum)"),
    ]
    
    for n, k, arr, expected, desc in tests:
        if run_test(n, k, arr, expected, desc):
            passed += 1
        total += 1
    
    # Maximum Constraints
    print("\n⚠️  Maximum constraint tests:")
    tests = [
        (100, 100000, [1000]*100, 1, "MAX: N=100, K=100000, all 1000s (K=sum)"),
        (100, 100000, [100000]*100, 350287504, "N=100, K=100000, all 100000s"),
        (50, 50000, [1000]*50, 1, "N=50, K=50000, all 1000s (K=sum)"),
    ]
    
    for n, k, arr, expected, desc in tests:
        if run_test(n, k, arr, expected, desc):
            passed += 1
        total += 1
    
    # Special Patterns
    print("\n[Special Patterns]")
    tests = [
        (5, 10, [0, 1, 2, 3, 4], 1, "Increasing: [0,1,2,3,4] (K=sum)"),
        (4, 8, [4, 3, 2, 1], 9, "Decreasing: [4,3,2,1]"),
        (3, 10, [0, 0, 10], 1, "Only last child can take: [0,0,10]"),
        (3, 10, [10, 0, 0], 1, "Only first child can take: [10,0,0]"),
    ]
    
    for n, k, arr, expected, desc in tests:
        if run_test(n, k, arr, expected, desc):
            passed += 1
        total += 1
    
    # Boundary Tests
    print("\n[Boundary Tests]")
    tests = [
        (1, 0, [0], 1, "Minimum: N=1, K=0, a[0]=0"),
        (100, 0, [0]*100, 1, "N=100 (max), K=0"),
        (1, 100000, [100000], 1, "K=100000 (max), single child"),
        (100, 100, [1]*100, 1, "N=100, K=100, all 1s"),
    ]
    
    for n, k, arr, expected, desc in tests:
        if run_test(n, k, arr, expected, desc):
            passed += 1
        total += 1
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Tests Passed: {passed}/{total}")
    
    print("\nComplexity Analysis:")
    print("  ✅ Time: O(N × K) - process each child for each candy count")
    print("  ✅ Space: O(N × K) - DP table and cumulative sum array")
    print("  ✅ Optimization: Prefix sums avoid O(N × K × max(a[i]))")
    print("  ✅ For N=100, K=100000: ~10^7 operations (fast)")
    print("  ✅ Modulo arithmetic: all operations mod 10^9+7")
    
    print("\nKey Insights:")
    print("  • dp[i][j] = ways to distribute j candies among first i children")
    print("  • Transition: sum dp[i-1][j-c] for c in [0, min(a[i-1], j)]")
    print("  • Prefix sums convert O(N×K×a[i]) to O(N×K)")
    print("  • Base case: dp[0][0] = 1 (one way to give 0 candies)")
    print("=" * 80)
    
    return 0 if passed == total else 1

if __name__ == "__main__":
    sys.exit(main())
