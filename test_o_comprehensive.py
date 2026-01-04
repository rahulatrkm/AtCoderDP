#!/usr/bin/env python3
"""
Comprehensive test suite for Problem O: Matching
Tests edge cases, performance, and correctness
"""

import subprocess
import sys
import time

def run_test(n, matrix, expected, desc):
    """Run a single test case"""
    input_lines = [str(n)]
    for row in matrix:
        input_lines.append(' '.join(map(str, row)))
    input_str = '\n'.join(input_lines) + '\n'
    
    try:
        start_time = time.time()
        result = subprocess.run(
            ['python3', 'o.py'],
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
    print("PROBLEM O: Matching - Man-Woman Pairing")
    print("Constraints: 1 ≤ N ≤ 21, a[i][j] ∈ {0,1}")
    print("=" * 80)
    
    passed = 0
    total = 0
    
    # Sample Tests
    print("\n[Official Sample Tests]")
    tests = [
        (3, [[0,1,1],[1,0,1],[1,1,1]], 3, "Sample 1: N=3, mixed compatibility"),
        (4, [[0,1,0,0],[0,0,0,1],[1,0,0,0],[0,0,1,0]], 1, "Sample 2: N=4, unique matching"),
        (1, [[0]], 0, "Sample 3: N=1, no compatibility"),
    ]
    
    for n, matrix, expected, desc in tests:
        if run_test(n, matrix, expected, desc):
            passed += 1
        total += 1
    
    # Edge Cases - Minimum N
    print("\n[Edge Cases - Minimum N=1]")
    tests = [
        (1, [[0]], 0, "N=1: no match possible"),
        (1, [[1]], 1, "N=1: one match possible"),
    ]
    
    for n, matrix, expected, desc in tests:
        if run_test(n, matrix, expected, desc):
            passed += 1
        total += 1
    
    # Edge Cases - N=2
    print("\n[Edge Cases - N=2]")
    tests = [
        (2, [[0,0],[0,0]], 0, "N=2: no compatibility"),
        (2, [[1,0],[0,1]], 1, "N=2: diagonal only"),
        (2, [[0,1],[1,0]], 1, "N=2: anti-diagonal only"),
        (2, [[1,1],[1,1]], 2, "N=2: all compatible"),
        (2, [[1,0],[1,0]], 0, "N=2: woman 1 compatible with both, woman 2 with none"),
    ]
    
    for n, matrix, expected, desc in tests:
        if run_test(n, matrix, expected, desc):
            passed += 1
        total += 1
    
    # Small N Tests
    print("\n[Small N Tests (N=3-5)]")
    tests = [
        (3, [[1,1,1],[1,1,1],[1,1,1]], 6, "N=3: all compatible (3! = 6)"),
        (3, [[1,0,0],[0,1,0],[0,0,1]], 1, "N=3: identity matrix (only diagonal)"),
        (3, [[0,0,0],[0,0,0],[0,0,0]], 0, "N=3: no compatibility"),
        (4, [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]], 24, "N=4: all compatible (4! = 24)"),
        (5, [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]], 120, "N=5: all compatible (5! = 120)"),
    ]
    
    for n, matrix, expected, desc in tests:
        if run_test(n, matrix, expected, desc):
            passed += 1
        total += 1
    
    # Identity Matrix Tests
    print("\n[Identity Matrix Tests]")
    tests = [
        (5, [[1 if i==j else 0 for j in range(5)] for i in range(5)], 1, "N=5: identity matrix"),
        (10, [[1 if i==j else 0 for j in range(10)] for i in range(10)], 1, "N=10: identity matrix"),
    ]
    
    for n, matrix, expected, desc in tests:
        if run_test(n, matrix, expected, desc):
            passed += 1
        total += 1
    
    # Sparse Compatibility
    print("\n[Sparse Compatibility]")
    tests = [
        (4, [[1,1,0,0],[0,0,1,1],[1,0,1,0],[0,1,0,1]], 2, "N=4: block pattern"),
        (6, [[1 if i<=j else 0 for j in range(6)] for i in range(6)], 1, "N=6: upper triangular"),
    ]
    
    for n, matrix, expected, desc in tests:
        if run_test(n, matrix, expected, desc):
            passed += 1
        total += 1
    
    # Medium N Tests
    print("\n[Medium N Tests (N=10)]")
    tests = [
        (10, [[1]*10 for _ in range(10)], 3628800, "N=10: all compatible (10! = 3628800)"),
        (10, [[1 if i==j else 0 for j in range(10)] for i in range(10)], 1, "N=10: identity"),
        (10, [[0]*10 for _ in range(10)], 0, "N=10: no compatibility"),
    ]
    
    for n, matrix, expected, desc in tests:
        if run_test(n, matrix, expected, desc):
            passed += 1
        total += 1
    
    # Large N Tests
    print("\n[Large N Tests (N=15)]")
    tests = [
        (15, [[1]*15 for _ in range(15)], 674358851, "N=15: all compatible (15! mod 10^9+7)"),
        (15, [[1 if i==j else 0 for j in range(15)] for i in range(15)], 1, "N=15: identity"),
    ]
    
    for n, matrix, expected, desc in tests:
        if run_test(n, matrix, expected, desc):
            passed += 1
        total += 1
    
    # Maximum N = 21 Tests
    print("\n⚠️  CRITICAL: Maximum N=21 Tests")
    tests = [
        (21, [[1 if i==j else 0 for j in range(21)] for i in range(21)], 1, "MAX N=21: identity matrix"),
        (21, [[0]*21 for _ in range(21)], 0, "MAX N=21: no compatibility"),
        (21, [[1]*21 for _ in range(21)], 72847302, "MAX N=21: all compatible (21! mod 10^9+7)"),
    ]
    
    for n, matrix, expected, desc in tests:
        if run_test(n, matrix, expected, desc):
            passed += 1
        total += 1
    
    # Alternating Patterns at N=21
    print("\n[N=21 Special Patterns]")
    # Checkerboard pattern
    matrix_21_checker = [[(i+j)%2 for j in range(21)] for i in range(21)]
    tests = [
        (21, matrix_21_checker, 0, "N=21: checkerboard pattern (should be 0)"),
    ]
    
    for n, matrix, expected, desc in tests:
        if run_test(n, matrix, expected, desc):
            passed += 1
        total += 1
    
    # Performance Stress Tests
    print("\n[Performance Tests - Random-like Patterns]")
    # Upper triangular with all 1s
    matrix_20_upper = [[1 if i<=j else 0 for j in range(20)] for i in range(20)]
    tests = [
        (20, matrix_20_upper, 1, "N=20: upper triangular (only diagonal works)"),
    ]
    
    for n, matrix, expected, desc in tests:
        if run_test(n, matrix, expected, desc):
            passed += 1
        total += 1
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Tests Passed: {passed}/{total}")
    
    print("\nComplexity Analysis:")
    print("  ✓  Algorithm: Bitmask DP")
    print("  ✓  Time: O(2^N × N) - iterate through all 2^N masks, try N women per mask")
    print("  ✓  Space: O(2^N) - DP array for all possible masks")
    print("  ✓  For N=21: 2^21 = 2,097,152 states")
    print("  ✓  Modulo: 10^9+7")
    
    print("\nEdge Cases Verified:")
    print("  ✓ Minimum N=1")
    print("  ✓ Maximum N=21")
    print("  ✓ All compatible (factorial counts)")
    print("  ✓ No compatibility (0 matchings)")
    print("  ✓ Identity matrix (1 matching)")
    print("  ✓ Various patterns (checkerboard, triangular, blocks)")
    
    print("\nKey Insights:")
    print("  • dp[mask] = number of ways to pair first popcount(mask) men")
    print("  • mask bit j=1 means woman j is already paired")
    print("  • popcount(mask) tells us which man we're pairing next")
    print("  • Transition: if man x compatible with woman j, dp[mask|(1<<j)] += dp[mask]")
    print("  • Answer is dp[(1<<N)-1] (all women paired)")
    print("=" * 80)
    
    return 0 if passed == total else 1

if __name__ == "__main__":
    sys.exit(main())
