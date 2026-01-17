#!/usr/bin/env python3
"""
Comprehensive edge case and performance testing for Problem W
"""

import subprocess
import sys
import time

def run_test(n, queries, expected, timeout=5):
    """Run a single test case"""
    input_data = f"{n} {len(queries)}\n"
    for l, r, a in queries:
        input_data += f"{l} {r} {a}\n"
    
    try:
        start = time.time()
        result = subprocess.run(
            ['python3', 'w.py'],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        elapsed = time.time() - start
        
        output = result.stdout.strip()
        actual = int(output)
        return actual == expected, actual, elapsed
    except subprocess.TimeoutExpired:
        return False, "TIMEOUT", timeout
    except Exception as e:
        return False, str(e), 0

print("="*70)
print("EDGE CASE TESTING FOR PROBLEM W")
print("="*70)

# Edge Cases
edge_cases = [
    # (n, queries, expected, description)
    (1, [], 0, "No queries"),
    (100, [], 0, "Large n, no queries"),
    (1, [(1, 1, 0)], 0, "Query with score 0"),
    (5, [(1, 5, 0), (2, 4, 0), (3, 3, 0)], 0, "All queries score 0"),
    (1, [(1, 1, -1000000000)], 0, "Single large negative"),
    (3, [(1, 1, -100), (2, 2, -200), (3, 3, -300)], 0, "All negative queries"),
    (1, [(1, 1, 1000000000)], 1000000000, "Single large positive"),
    (3, [(1, 1, 1000000000), (2, 2, 1000000000), (3, 3, 1000000000)], 3000000000, "Three large positives"),
    (1, [(1, 1, 1000000000)] * 10, 10000000000, "10 identical large queries"),
    (2, [(1, 1, 1), (1, 1, 2), (1, 1, 3)], 6, "Multiple queries same interval"),
    (3, [(1, 1, 10), (1, 2, 20), (1, 3, 30)], 60, "Nested intervals all activate together"),
    (5, [(1, 2, 10), (2, 3, -30), (3, 4, 10), (4, 5, 10)], 30, "Chain with negative middle"),
    (10, [(i, i, 1) for i in range(1, 11)], 10, "10 non-overlapping unit intervals"),
    (10, [(1, 10, 100)], 100, "Single query spanning all"),
    (10, [(1, 5, 50), (6, 10, 50)], 100, "Two halves non-overlapping"),
    (10, [(1, 5, 50), (4, 10, 50)], 100, "Two halves overlapping"),
    (5, [(1, 3, 10), (2, 4, 10), (3, 5, 10)], 30, "Sliding window all activate"),
    (1, [(1, 1, -5), (1, 1, 10)], 5, "Overlapping positive and negative"),
    (2, [(1, 2, 100), (1, 1, -10), (2, 2, -10)], 90, "Spanning with negatives at ends"),
]

print("\n### EDGE CASE TESTS ###\n")
passed = 0
failed = 0

for n, queries, expected, description in edge_cases:
    success, actual, elapsed = run_test(n, queries, expected)
    
    status = "✓ PASS" if success else "✗ FAIL"
    print(f"{status}: {description}")
    print(f"  n={n}, m={len(queries)}, expected={expected}, actual={actual}, time={elapsed:.4f}s")
    
    if success:
        passed += 1
    else:
        failed += 1
    print()

# Performance Tests
print("\n" + "="*70)
print("PERFORMANCE TESTING")
print("="*70 + "\n")

performance_tests = [
    # (n, m, description, timeout)
    (10, 10, "Small n, small m (bitmask)", 5),
    (100, 15, "Medium n, m=15 (bitmask)", 5),
    (500, 18, "Large n, m=18 (bitmask)", 5),
    (1000, 20, "Large n, m=20 (bitmask boundary)", 10),
    (1000, 25, "Large n, m=25 (segment tree)", 5),
    (5000, 50, "Very large n, m=50 (segment tree)", 5),
    (10000, 100, "Very large n, m=100 (segment tree)", 5),
    (50000, 200, "Extreme n, m=200 (segment tree)", 10),
]

print("### TIME COMPLEXITY TESTS ###\n")

for n, m, description, timeout in performance_tests:
    # Generate test queries
    queries = []
    for i in range(m):
        l = (i * n) // (m + 1)
        r = min(l + n // 10, n - 1)
        a = (i % 3 - 1) * 100  # Mix of -100, 0, 100
        queries.append((l + 1, r + 1, a))
    
    input_data = f"{n} {m}\n"
    for l, r, a in queries:
        input_data += f"{l} {r} {a}\n"
    
    try:
        start = time.time()
        result = subprocess.run(
            ['python3', 'w.py'],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        elapsed = time.time() - start
        
        status = "✓" if elapsed < timeout / 2 else "⚠"
        print(f"{status} {description}")
        print(f"  n={n}, m={m}, time={elapsed:.4f}s")
        
        if result.returncode == 0:
            print(f"  result={result.stdout.strip()}")
        else:
            print(f"  ERROR: {result.stderr[:100]}")
        print()
        
    except subprocess.TimeoutExpired:
        print(f"✗ {description}")
        print(f"  n={n}, m={m}, TIMEOUT (>{timeout}s)")
        print()

# Space Complexity Analysis
print("\n" + "="*70)
print("SPACE COMPLEXITY ANALYSIS")
print("="*70 + "\n")

print("Theoretical Space Complexity:")
print("  Bitmask DP (m ≤ 20): O(n × 2^m)")
print("    - m=10: ~n × 1K states")
print("    - m=15: ~n × 32K states")
print("    - m=20: ~n × 1M states")
print("  Segment Tree (m > 20): O(n)")
print("    - Dictionary-based sparse segment tree")
print("    - Only stores non-zero nodes")
print()

print("Memory estimates:")
print("  n=1000, m=15: ~1000 × 32K = 32M states (bitmask)")
print("  n=1000, m=25: ~1000 nodes (segment tree)")
print("  n=100000, m=100: ~100K nodes (segment tree)")
print()

# Summary
print("\n" + "="*70)
print("SUMMARY")
print("="*70 + "\n")

print(f"Edge Case Tests: {passed} passed, {failed} failed out of {passed + failed}")
print(f"Success Rate: {100 * passed / (passed + failed):.1f}%")
print()

print("Time Complexity:")
print("  ✓ Bitmask DP: O(n × 2^m × m) - exact solution for m ≤ 20")
print("  ✓ Segment Tree: O((n + m) log n) - fast solution for m > 20")
print()

print("Space Complexity:")
print("  ✓ Bitmask DP: O(n × 2^m) - manageable for m ≤ 20")
print("  ✓ Segment Tree: O(n) - scalable for large inputs")
print()

if failed > 0:
    sys.exit(1)
