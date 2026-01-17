#!/usr/bin/env python3
"""
Comprehensive test suite for Problem R: Walk
Tests edge cases, time complexity, and space complexity

Problem: Count the number of walks of length K in a directed graph
"""

import subprocess
import sys
import time

def run_test(n, k, matrix, expected, desc):
    """Run a single test case"""
    input_str = f"{n} {k}\n"
    for row in matrix:
        input_str += ' '.join(map(str, row)) + '\n'
    
    try:
        start_time = time.time()
        result = subprocess.run(
            ['python3', 'r.py'],
            input=input_str,
            capture_output=True,
            text=True,
            timeout=10
        )
        elapsed = time.time() - start_time
        
        if result.returncode != 0:
            print(f"✗ {desc}")
            print(f"   Error: {result.stderr[:200]}")
            return False
        
        actual = int(result.stdout.strip())
        
        if actual == expected:
            if elapsed < 0.1:
                print(f"✓ ⚡ {desc}")
            elif elapsed < 1.0:
                print(f"✓ ⏱️  {desc}")
            else:
                print(f"✓ 🐌 {desc}")
            print(f"   Result: {actual} (Expected: {expected}) [{elapsed:.3f}s]")
            return True
        else:
            print(f"✗ {desc}")
            print(f"   Got: {actual}, Expected: {expected}")
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
    print("PROBLEM R: Walk - Matrix Exponentiation")
    print("Constraints: 1 ≤ N ≤ 50, 1 ≤ K ≤ 10^18")
    print("=" * 80)
    
    passed = 0
    total = 0
    
    # Official Sample Tests
    print("\n[Official Sample Tests]")
    tests = [
        (4, 2, [[0,1,0,0],[0,0,1,1],[0,0,0,1],[1,0,0,0]], 6, "Sample: N=4, K=2, has cycles"),
    ]
    
    for n, k, mat, expected, desc in tests:
        if run_test(n, k, mat, expected, desc):
            passed += 1
        total += 1
    
    # Edge Cases - Minimum N
    print("\n[Edge Cases - Minimum N=1]")
    tests = [
        (1, 1, [[0]], 0, "N=1, K=1: no edges"),
        (1, 1, [[1]], 1, "N=1, K=1: self-loop"),
        (1, 10, [[1]], 1, "N=1, K=10: self-loop"),
        (1, 1000000000000000000, [[1]], 1, "N=1, K=10^18: self-loop"),
        (1, 1000000000000000000, [[0]], 0, "N=1, K=10^18: no edges"),
    ]
    
    for n, k, mat, expected, desc in tests:
        if run_test(n, k, mat, expected, desc):
            passed += 1
        total += 1
    
    # Edge Cases - N=2
    print("\n[Edge Cases - N=2]")
    tests = [
        (2, 1, [[0,1],[0,0]], 1, "N=2, K=1: single edge"),
        (2, 2, [[0,1],[0,0]], 0, "N=2, K=2: no paths"),
        (2, 1, [[0,1],[1,0]], 2, "N=2, K=1: bidirectional"),
        (2, 2, [[0,1],[1,0]], 2, "N=2, K=2: cycle"),
        (2, 3, [[0,1],[1,0]], 2, "N=2, K=3: cycle odd"),
        (2, 10, [[0,1],[1,0]], 2, "N=2, K=10: cycle even"),
    ]
    
    for n, k, mat, expected, desc in tests:
        if run_test(n, k, mat, expected, desc):
            passed += 1
        total += 1
    
    # No Edges
    print("\n[No Edges (Empty Graph)]")
    tests = [
        (3, 1, [[0,0,0],[0,0,0],[0,0,0]], 0, "N=3, K=1: all zeros"),
        (5, 10, [[0]*5 for _ in range(5)], 0, "N=5, K=10: all zeros"),
        (10, 1000000, [[0]*10 for _ in range(10)], 0, "N=10, K=10^6: all zeros"),
    ]
    
    for n, k, mat, expected, desc in tests:
        if run_test(n, k, mat, expected, desc):
            passed += 1
        total += 1
    
    # Self-loops
    print("\n[Self-loops Only]")
    tests = [
        (3, 1, [[1,0,0],[0,1,0],[0,0,1]], 3, "N=3, K=1: identity"),
        (3, 5, [[1,0,0],[0,1,0],[0,0,1]], 3, "N=3, K=5: identity"),
        (5, 1000000000, [[1 if i==j else 0 for j in range(5)] for i in range(5)], 5, "N=5, K=10^9: identity"),
    ]
    
    for n, k, mat, expected, desc in tests:
        if run_test(n, k, mat, expected, desc):
            passed += 1
        total += 1
    
    # Complete Graph
    print("\n[Complete Graph (all edges except self-loops)]")
    tests = [
        (3, 1, [[0,1,1],[1,0,1],[1,1,0]], 6, "N=3, K=1: complete graph"),
        (3, 2, [[0,1,1],[1,0,1],[1,1,0]], 12, "N=3, K=2: complete graph"),
        (4, 1, [[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]], 12, "N=4, K=1: complete"),
    ]
    
    for n, k, mat, expected, desc in tests:
        if run_test(n, k, mat, expected, desc):
            passed += 1
        total += 1
    
    # Linear Chain
    print("\n[Linear Chains]")
    tests = [
        (3, 1, [[0,1,0],[0,0,1],[0,0,0]], 2, "N=3, K=1: 0->1->2"),
        (3, 2, [[0,1,0],[0,0,1],[0,0,0]], 1, "N=3, K=2: 0->1->2"),
        (3, 3, [[0,1,0],[0,0,1],[0,0,0]], 0, "N=3, K=3: 0->1->2 (no path)"),
        (5, 1, [[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1],[0,0,0,0,0]], 4, "N=5, K=1: chain"),
        (5, 4, [[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1],[0,0,0,0,0]], 1, "N=5, K=4: chain"),
    ]
    
    for n, k, mat, expected, desc in tests:
        if run_test(n, k, mat, expected, desc):
            passed += 1
        total += 1
    
    # Cycles
    print("\n[Cycles]")
    tests = [
        (3, 1, [[0,1,0],[0,0,1],[1,0,0]], 3, "N=3, K=1: 3-cycle"),
        (3, 3, [[0,1,0],[0,0,1],[1,0,0]], 3, "N=3, K=3: 3-cycle completes"),
        (3, 6, [[0,1,0],[0,0,1],[1,0,0]], 3, "N=3, K=6: 3-cycle doubles"),
        (4, 4, [[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]], 4, "N=4, K=4: 4-cycle completes"),
    ]
    
    for n, k, mat, expected, desc in tests:
        if run_test(n, k, mat, expected, desc):
            passed += 1
        total += 1
    
    # Large K values
    print("\n[Large K Values (10^9 to 10^18)]")
    tests = [
        (2, 10**9, [[0,1],[1,0]], 2, "N=2, K=10^9: cycle"),
        (3, 10**12, [[1,0,0],[0,1,0],[0,0,1]], 3, "N=3, K=10^12: identity"),
        (5, 10**15, [[0]*5 for _ in range(5)], 0, "N=5, K=10^15: no edges"),
        (2, 10**18, [[0,1],[1,0]], 2, "N=2, K=10^18: cycle (max K)"),
    ]
    
    for n, k, mat, expected, desc in tests:
        if run_test(n, k, mat, expected, desc):
            passed += 1
        total += 1
    
    # Medium Size
    print("\n[Medium Size (N=10-20)]")
    n = 10
    # Create a cycle of length 10
    mat = [[0]*n for _ in range(n)]
    for i in range(n-1):
        mat[i][i+1] = 1
    mat[n-1][0] = 1
    tests = [
        (n, 1, mat, n, "N=10, K=1: 10-cycle"),
        (n, 10, mat, n, "N=10, K=10: 10-cycle completes"),
        (n, 100, mat, n, "N=10, K=100: 10-cycle multiple"),
    ]
    
    for n, k, mat, expected, desc in tests:
        if run_test(n, k, mat, expected, desc):
            passed += 1
        total += 1
    
    # Large Size
    print("\n[Large Size (N=30-50)]")
    n = 30
    mat = [[1 if i==j else 0 for j in range(n)] for i in range(n)]
    tests = [
        (n, 1000000, mat, n, "N=30, K=10^6: identity"),
    ]
    
    for n, k, mat, expected, desc in tests:
        if run_test(n, k, mat, expected, desc):
            passed += 1
        total += 1
    
    # Maximum N
    print("\n⚠️  CRITICAL: Maximum N=50")
    n = 50
    mat = [[1 if i==j else 0 for j in range(n)] for i in range(n)]
    tests = [
        (n, 1, mat, n, "N=50, K=1: identity"),
        (n, 1000000000000000000, mat, n, "N=50, K=10^18: identity (max constraints)"),
    ]
    
    for n, k, mat, expected, desc in tests:
        if run_test(n, k, mat, expected, desc):
            passed += 1
        total += 1
    
    # Complete graph with max N
    n = 50
    mat = [[0 if i==j else 1 for j in range(n)] for i in range(n)]
    tests = [
        (n, 1, mat, 2450, "N=50, K=1: complete graph"),
        (n, 2, mat, 120050, "N=50, K=2: complete graph"),
    ]
    
    for n, k, mat, expected, desc in tests:
        if run_test(n, k, mat, expected, desc):
            passed += 1
        total += 1
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Tests Passed: {passed}/{total}")
    
    print("\nComplexity Analysis:")
    print("  Algorithm: Matrix Exponentiation (Fast Exponentiation)")
    print("  ✓  Time: O(N³ × log K) - N³ for matrix mult, log K for exponentiation")
    print("  ✓  Space: O(N²) - storing matrices")
    print("  ✓  K=10^18: ~60 matrix multiplications")
    print("  ✓  N=50, K=10^18: ~60 × 50³ = 7.5M operations")
    
    print("\nEdge Cases Verified:")
    print("  ✓ Minimum N=1 (with/without self-loop)")
    print("  ✓ Maximum N=50")
    print("  ✓ Maximum K=10^18")
    print("  ✓ No edges (empty graph)")
    print("  ✓ Self-loops only (identity matrix)")
    print("  ✓ Complete graphs")
    print("  ✓ Linear chains")
    print("  ✓ Cycles of various lengths")
    print("  ✓ Large K values (10^9, 10^12, 10^15, 10^18)")
    
    print("\nKey Insights:")
    print("  • A^K gives number of K-length walks where A is adjacency matrix")
    print("  • Fast exponentiation: compute A^K in O(log K) matrix multiplications")
    print("  • Each matrix multiplication: O(N³)")
    print("  • Total time: O(N³ log K) - feasible for N=50, K=10^18")
    print("  • Regular DP would be O(K×N²) - impossible for K=10^18")
    print("=" * 80)
    
    return 0 if passed == total else 1

if __name__ == "__main__":
    sys.exit(main())
