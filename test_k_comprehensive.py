#!/usr/bin/env python3
"""
Comprehensive test suite for Problem K: Stones
https://atcoder.jp/contests/dp/tasks/dp_k

Problem: Game theory - two players take turns removing stones.
Given K stones and N possible moves, determine if first player wins.

Constraints:
- 1 ≤ N ≤ 100
- 1 ≤ K ≤ 10^5
- 1 ≤ ai ≤ K

Expected Complexity:
- Time: O(N * K) - for each position check all moves
- Space: O(K) - DP array for all positions
"""

import subprocess
import time
import sys

def run_test(n, k, moves, expected, description):
    """Run a single test case"""
    input_data = f"{n} {k}\n{' '.join(map(str, moves))}\n"
    
    try:
        start = time.time()
        result = subprocess.run(
            ['python3', 'k.py'],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=5
        )
        elapsed = time.time() - start
        
        if result.returncode != 0:
            print(f"✗ {description}: CRASHED")
            print(f"   Error: {result.stderr[:200]}")
            return False
        
        output = result.stdout.strip()
        
        if output == expected:
            speed = "⚡" if elapsed < 0.1 else "⏱️" if elapsed < 1.0 else "🐌"
            print(f"✓ {speed} {description}")
            print(f"   Result: {output} (Expected: {expected}) [{elapsed:.3f}s]")
            return True
        else:
            print(f"✗ {description}")
            print(f"   Result: {output} (Expected: {expected}) [{elapsed:.3f}s]")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"✗ {description}: TIMEOUT (>5s)")
        return False
    except Exception as e:
        print(f"✗ {description}: ERROR - {str(e)}")
        return False

def main():
    print("=" * 80)
    print("PROBLEM K: Stones - Game Theory (Nim-like)")
    print("Constraints: N ≤ 100, K ≤ 10^5")
    print("=" * 80)
    
    passed = 0
    total = 0
    
    # Sample Tests
    print("\n[Sample Tests]")
    tests = [
        (2, 4, [2, 3], "First", "Sample 1: K=4, moves=[2,3]"),
        (2, 5, [2, 3], "Second", "Sample 2: K=5, moves=[2,3]"),
        (2, 7, [2, 3], "First", "Sample 3: K=7, moves=[2,3]"),
        (1, 1, [1], "First", "Sample 4: K=1, move=[1]"),
    ]
    
    for n, k, moves, expected, desc in tests:
        if run_test(n, k, moves, expected, desc):
            passed += 1
        total += 1
    
    # Edge Cases - Small K
    print("\n[Edge Cases - Small K]")
    tests = [
        (1, 1, [1], "First", "K=1, can take 1"),
        (1, 2, [1], "Second", "K=2, opponent gets winning position"),
        (1, 3, [1], "First", "K=3, take 1 → opponent at K=2"),
        (2, 1, [1, 2], "First", "K=1, multiple moves available"),
        (2, 2, [1, 2], "First", "K=2, can take all"),
        (3, 3, [1, 2, 3], "First", "K=3, can take all"),
        (3, 4, [1, 2, 3], "Second", "K=4, all moves lead to winning for opponent"),
    ]
    
    for n, k, moves, expected, desc in tests:
        if run_test(n, k, moves, expected, desc):
            passed += 1
        total += 1
    
    # Pattern Recognition Tests
    print("\n[Pattern Recognition - Nim Game]")
    tests = [
        # Move size = 1: Odd K wins, Even K loses
        (1, 5, [1], "First", "Move=1, K=5 (odd): first wins"),
        (1, 10, [1], "Second", "Move=1, K=10 (even): second wins"),
        (1, 100, [1], "Second", "Move=1, K=100 (even): second wins"),
        (1, 101, [1], "First", "Move=1, K=101 (odd): first wins"),
        
        # Move sizes = [1, 2]: Pattern with multiples of 3
        # Losing positions: 0, 3, 6, 9, 12... (multiples of 3)
        (2, 6, [1, 2], "Second", "Moves=[1,2], K=6: losing position"),
        (2, 9, [1, 2], "Second", "Moves=[1,2], K=9: losing position"),
        (2, 12, [1, 2], "Second", "Moves=[1,2], K=12: losing position"),
        (2, 8, [1, 2], "First", "Moves=[1,2], K=8: winning position"),
        (2, 10, [1, 2], "First", "Moves=[1,2], K=10: winning position"),
        
        # Move sizes = [2, 3]: Different pattern
        (2, 1, [2, 3], "Second", "Moves=[2,3], K=1: can't move"),
        (2, 2, [2, 3], "First", "Moves=[2,3], K=2: take 2"),
        (2, 3, [2, 3], "First", "Moves=[2,3], K=3: take 3"),
    ]
    
    for n, k, moves, expected, desc in tests:
        if run_test(n, k, moves, expected, desc):
            passed += 1
        total += 1
    
    # Large K Tests
    print("\n[Large K Tests - Performance]")
    tests = [
        (1, 1000, [1], "Second", "K=1000 (even), move=1"),
        (1, 10000, [1], "Second", "K=10000 (even), move=1"),
        (2, 1000, [1, 2], "First", "K=1000, moves=[1,2]"),
        (3, 1000, [1, 2, 3], "Second", "K=1000, moves=[1,2,3]"),
        (5, 5000, [1, 2, 3, 4, 5], "First", "K=5000, moves=[1,2,3,4,5]"),
        (10, 10000, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "First", "K=10000, 10 moves"),
    ]
    
    for n, k, moves, expected, desc in tests:
        if run_test(n, k, moves, expected, desc):
            passed += 1
        total += 1
    
    # Maximum Constraints
    print("\n⚠️  Maximum constraint tests:")
    tests = [
        (100, 100000, list(range(1, 101)), "First", "MAX: N=100, K=100000, moves=1..100"),
        (100, 99999, list(range(1, 101)), "First", "N=100, K=99999, moves=1..100"),
        (50, 100000, list(range(1, 51)), "First", "N=50, K=100000, moves=1..50"),
    ]
    
    for n, k, moves, expected, desc in tests:
        if run_test(n, k, moves, expected, desc):
            passed += 1
        total += 1
    
    # Special Patterns
    print("\n[Special Cases]")
    tests = [
        # Large gaps in moves
        (2, 10, [2, 5], "First", "Moves=[2,5], K=10"),
        (2, 11, [2, 5], "Second", "Moves=[2,5], K=11"),
        (3, 20, [3, 5, 7], "Second", "Large prime moves"),
        
        # All same move
        (3, 6, [2, 2, 2], "First", "All moves same: [2,2,2]"),
        
        # Move equals K
        (1, 50, [50], "First", "Move equals K: instant win"),
        (2, 50, [25, 50], "First", "One move equals K"),
        
        # Large single move
        (1, 100, [99], "First", "K=100, move=99"),
        (2, 100, [1, 99], "Second", "K=100 (even), moves=[1,99]"),
    ]
    
    for n, k, moves, expected, desc in tests:
        if run_test(n, k, moves, expected, desc):
            passed += 1
        total += 1
    
    # Boundary Tests
    print("\n[Boundary Tests]")
    tests = [
        (1, 1, [1], "First", "Minimum: N=1, K=1, move=1"),
        (100, 1, [1]*100, "First", "N=100 (max), K=1, all moves=1"),
        (1, 100000, [1], "Second", "K=100000 (even max), move=1"),
        (1, 100000, [100000], "First", "K=100000, move=100000 (max)"),
    ]
    
    for n, k, moves, expected, desc in tests:
        if run_test(n, k, moves, expected, desc):
            passed += 1
        total += 1
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Tests Passed: {passed}/{total}")
    
    print("\nComplexity Analysis:")
    print("  ✅ Time: O(N × K) - for each position, check all N moves")
    print("  ✅ Space: O(K) - DP array storing win/lose for each position")
    print("  ✅ For K=100000, N=100: ~10^7 operations (fast)")
    print("  ✅ Iterative DP avoids recursion depth issues")
    print("  ✅ Game Theory: Grundy numbers / Nim-like game")
    print("\nKey Insights:")
    print("  • Position is winning if ANY move leads to losing position")
    print("  • Position is losing if ALL moves lead to winning positions")
    print("  • Base case: position 0 is losing (no moves available)")
    print("=" * 80)
    
    return 0 if passed == total else 1

if __name__ == "__main__":
    sys.exit(main())
