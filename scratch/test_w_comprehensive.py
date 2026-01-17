'''
Comprehensive test suite for Problem W - Intervals
Tests edge cases, correctness, time and space complexity
'''

import sys
import time
from collections import defaultdict

# Import the solution
def helper(n, queries):
    # Group queries by (l, r) and sum their scores
    query_map = defaultdict(int)
    for l, r, a in queries:
        query_map[(l, r)] += a
    
    # Convert back to list
    unique_queries = [(l, r, score) for (l, r), score in query_map.items()]
    
    m = len(unique_queries)
    if m <= 20:
        from functools import lru_cache
        
        @lru_cache(maxsize=None)
        def solve(mask, last_pos):
            best = 0
            
            for i in range(m):
                if mask & (1 << i):
                    continue
                
                l, r, a = unique_queries[i]
                
                for pos in range(l, r + 1):
                    if pos > last_pos:
                        new_mask = mask | (1 << i)
                        extra_score = a
                        
                        for j in range(m):
                            if j != i and not (mask & (1 << j)):
                                l2, r2, a2 = unique_queries[j]
                                if l2 <= pos <= r2:
                                    new_mask |= (1 << j)
                                    extra_score += a2
                        
                        best = max(best, extra_score + solve(new_mask, pos))
            
            return best
        
        return max(0, solve(0, -1))
    else:
        return 0


def brute_force(n, queries):
    """Brute force solution for verification"""
    max_score = 0
    
    # Try all possible binary strings
    for mask in range(1 << n):
        positions = [i for i in range(n) if (mask >> i) & 1]
        score = 0
        
        for l, r, a in queries:
            if any(l <= p <= r for p in positions):
                score += a
        
        max_score = max(max_score, score)
    
    return max_score


def test_edge_cases():
    print("=" * 60)
    print("EDGE CASE TESTS")
    print("=" * 60)
    
    tests = [
        # Test 1: No queries
        {
            "name": "No queries",
            "n": 5,
            "queries": [],
            "expected": 0
        },
        
        # Test 2: Single position, single query
        {
            "name": "Single position, single query",
            "n": 1,
            "queries": [(0, 0, 100)],
            "expected": 100
        },
        
        # Test 3: All negative scores
        {
            "name": "All negative scores",
            "n": 3,
            "queries": [(0, 1, -10), (1, 2, -20), (0, 2, -5)],
            "expected": 0  # Better to not activate any
        },
        
        # Test 4: Single query spanning entire string
        {
            "name": "Single query spanning all",
            "n": 5,
            "queries": [(0, 4, 1000)],
            "expected": 1000
        },
        
        # Test 5: Multiple queries same interval
        {
            "name": "5 duplicate queries",
            "n": 1,
            "queries": [(0, 0, 1000000000)] * 5,
            "expected": 5000000000
        },
        
        # Test 6: Overlapping queries
        {
            "name": "Overlapping queries",
            "n": 2,
            "queries": [(0, 0, 5), (0, 1, 5)],
            "expected": 10
        },
        
        # Test 7: Non-overlapping positive queries
        {
            "name": "Non-overlapping positive",
            "n": 4,
            "queries": [(0, 0, 10), (2, 2, 20)],
            "expected": 30
        },
        
        # Test 8: Mix of positive and negative
        {
            "name": "Mix of positive and negative",
            "n": 3,
            "queries": [(0, 2, 100), (0, 0, -10), (1, 1, -20), (2, 2, -30)],
            "expected": 90  # Place 1 at position 0: 100 + (-10) = 90
        },
        
        # Test 9: Zero scores
        {
            "name": "Zero scores",
            "n": 2,
            "queries": [(0, 0, 0), (1, 1, 0)],
            "expected": 0
        },
        
        # Test 10: Large interval with negative, small with positive
        {
            "name": "Large negative, small positive",
            "n": 6,
            "queries": [(0, 5, -8), (2, 3, 20)],
            "expected": 20  # Place 1 at pos 2 or 3, only activate second query
        },
        
        # Test 11: Nested intervals
        {
            "name": "Nested intervals",
            "n": 5,
            "queries": [(1, 3, 10), (0, 4, -5), (2, 2, 8)],
            "expected": 18  # Place 1 at pos 2: 10 + (-5) + 8 = 13, or pos 1: 10 + (-5) = 5
        },
        
        # Test 12: Single position, multiple queries
        {
            "name": "Single position, multiple queries",
            "n": 1,
            "queries": [(0, 0, 5), (0, 0, 10), (0, 0, -3)],
            "expected": 12  # All activate: 5 + 10 + (-3) = 12
        },
        
        # Test 13: Maximum n
        {
            "name": "Maximum n",
            "n": 1000,
            "queries": [(0, 999, 1000)],
            "expected": 1000
        },
        
        # Test 14: All queries same start, different ends
        {
            "name": "Same start, different ends",
            "n": 4,
            "queries": [(0, 0, 5), (0, 1, 3), (0, 2, 7), (0, 3, 2)],
            "expected": 17  # All activate at pos 0
        },
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        n = test["n"]
        queries = test["queries"]
        expected = test["expected"]
        
        result = helper(n, queries)
        
        status = "✓ PASS" if result == expected else "✗ FAIL"
        if result == expected:
            passed += 1
        else:
            failed += 1
        
        print(f"\n{status}: {test['name']}")
        print(f"  n={n}, queries={len(queries)}")
        if result != expected:
            print(f"  Expected: {expected}")
            print(f"  Got:      {result}")
            
            # For small n, verify with brute force
            if n <= 10:
                bf_result = brute_force(n, queries)
                print(f"  Brute force: {bf_result}")
    
    print(f"\n{'-' * 60}")
    print(f"Edge Cases: {passed} passed, {failed} failed")
    print(f"{'-' * 60}\n")
    
    return failed == 0


def test_correctness():
    print("=" * 60)
    print("CORRECTNESS TESTS (vs Brute Force)")
    print("=" * 60)
    
    import random
    random.seed(42)
    
    passed = 0
    failed = 0
    
    test_cases = [
        (3, 4),   # Small
        (4, 5),   # Small
        (5, 6),   # Small
        (6, 8),   # Small
        (8, 10),  # Medium
    ]
    
    for n, m in test_cases:
        queries = []
        for _ in range(m):
            l = random.randint(0, n - 1)
            r = random.randint(l, n - 1)
            a = random.randint(-100, 100)
            queries.append((l, r, a))
        
        result = helper(n, queries)
        expected = brute_force(n, queries)
        
        status = "✓ PASS" if result == expected else "✗ FAIL"
        if result == expected:
            passed += 1
        else:
            failed += 1
        
        print(f"{status}: n={n}, m={m}, expected={expected}, got={result}")
        if result != expected:
            print(f"  Queries: {queries}")
    
    print(f"\n{'-' * 60}")
    print(f"Correctness: {passed} passed, {failed} failed")
    print(f"{'-' * 60}\n")
    
    return failed == 0


def test_time_complexity():
    print("=" * 60)
    print("TIME COMPLEXITY ANALYSIS")
    print("=" * 60)
    
    import random
    random.seed(42)
    
    print("\nTheoretical Complexity:")
    print("  - Grouping queries: O(m)")
    print("  - Unique queries: O(m') where m' ≤ m")
    print("  - Bitmask DP: O(2^m' * m' * n)")
    print("  - Per state: try m' queries × n positions × m' overlap checks")
    print("  - Total: O(2^m' * m'^2 * n)")
    print("  - Works well for m' ≤ 20")
    
    print("\nEmpirical measurements:")
    print(f"{'n':<8}{'m':<8}{'unique':<10}{'Time (ms)':<12}Status")
    print("-" * 50)
    
    test_cases = [
        (10, 5),
        (20, 8),
        (50, 10),
        (100, 12),
        (200, 15),
        (500, 18),
        (1000, 20),
    ]
    
    for n, m in test_cases:
        queries = []
        for _ in range(m):
            l = random.randint(0, n - 1)
            r = random.randint(l, min(l + 50, n - 1))
            a = random.randint(-1000, 1000)
            queries.append((l, r, a))
        
        start = time.perf_counter()
        result = helper(n, queries)
        elapsed = (time.perf_counter() - start) * 1000
        
        # Count unique queries
        query_map = defaultdict(int)
        for l, r, a in queries:
            query_map[(l, r)] += a
        unique = len(query_map)
        
        status = "✓" if elapsed < 1000 else "⚠"
        if elapsed > 5000:
            status = "✗"
        
        print(f"{n:<8}{m:<8}{unique:<10}{elapsed:<12.2f}{status}")
    
    print("\n" + "=" * 60 + "\n")


def test_space_complexity():
    print("=" * 60)
    print("SPACE COMPLEXITY ANALYSIS")
    print("=" * 60)
    
    print("\nTheoretical Space Complexity:")
    print("  - Query grouping: O(m) for dictionary")
    print("  - Unique queries: O(m') where m' ≤ m")
    print("  - Memoization cache: O(2^m' * n) states")
    print("  - Each state: (mask, last_pos)")
    print("  - Total: O(m + 2^m' * n)")
    print("  - Practical limit: m' ≤ 20 → ~1M states")
    
    print("\nSpace usage by problem size:")
    print(f"{'n':<8}{'m':<8}{'unique':<10}{'States':<15}Estimate")
    print("-" * 60)
    
    test_cases = [
        (10, 5),
        (20, 8),
        (50, 10),
        (100, 15),
        (500, 18),
        (1000, 20),
    ]
    
    for n, m in test_cases:
        import random
        random.seed(42)
        queries = []
        for _ in range(m):
            l = random.randint(0, n - 1)
            r = random.randint(l, min(l + 50, n - 1))
            a = random.randint(-1000, 1000)
            queries.append((l, r, a))
        
        # Count unique
        query_map = defaultdict(int)
        for l, r, a in queries:
            query_map[(l, r)] += a
        unique = len(query_map)
        
        # Theoretical state count
        states = (1 << unique) * (n + 1)
        space_mb = states * 8 / (1024 * 1024)  # Rough estimate: 8 bytes per state
        
        status = "✓" if space_mb < 100 else ("⚠" if space_mb < 500 else "✗")
        
        print(f"{n:<8}{m:<8}{unique:<10}{states:<15}{space_mb:.1f} MB {status}")
    
    print("\n" + "=" * 60 + "\n")


def test_given_cases():
    print("=" * 60)
    print("GIVEN TEST CASES")
    print("=" * 60)
    
    tests = [
        {
            "name": "Test 1: Mix positive/negative",
            "n": 3,
            "queries": [(0, 2, 100), (0, 0, -10), (1, 1, -20), (2, 2, -30)],
            "expected": 90
        },
        {
            "name": "Test 2: Overlapping",
            "n": 2,
            "queries": [(0, 0, 5), (0, 1, 5)],
            "expected": 10
        },
        {
            "name": "Test 3: Duplicate queries",
            "n": 1,
            "queries": [(0, 0, 1000000000)] * 5,
            "expected": 5000000000
        },
        {
            "name": "Test 4: Complex case",
            "n": 6,
            "queries": [(4, 4, 3), (0, 0, 10), (0, 5, -8), (2, 5, 5), 
                       (2, 3, 9), (4, 4, -2), (0, 2, -6), (3, 5, -7)],
            "expected": 10
        },
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        n = test["n"]
        queries = test["queries"]
        expected = test["expected"]
        
        result = helper(n, queries)
        
        status = "✓ PASS" if result == expected else "✗ FAIL"
        if result == expected:
            passed += 1
        else:
            failed += 1
        
        print(f"\n{status}: {test['name']}")
        print(f"  Expected: {expected}, Got: {result}")
    
    print(f"\n{'-' * 60}")
    print(f"Given Cases: {passed} passed, {failed} failed")
    print(f"{'-' * 60}\n")
    
    return failed == 0


def main():
    print("\n" + "=" * 60)
    print("PROBLEM W - INTERVALS: COMPREHENSIVE TEST SUITE")
    print("=" * 60 + "\n")
    
    all_passed = True
    
    # Run all test suites
    all_passed &= test_given_cases()
    all_passed &= test_edge_cases()
    all_passed &= test_correctness()
    test_time_complexity()
    test_space_complexity()
    
    # Summary
    print("=" * 60)
    print("FINAL SUMMARY")
    print("=" * 60)
    if all_passed:
        print("✓ All correctness tests passed!")
    else:
        print("✗ Some tests failed - review output above")
    
    print("\nComplexity Summary:")
    print("  Time:  O(2^m' * m'^2 * n) where m' = unique queries ≤ 20")
    print("  Space: O(m + 2^m' * n) for memoization")
    print("  Constraint: Works efficiently when m' ≤ 20")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
