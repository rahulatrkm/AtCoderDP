#!/usr/bin/env python3
"""
Test suite for Problem W - Intervals
"""

import subprocess
import sys

def run_test(n, queries, expected):
    """Run a single test case"""
    input_data = f"{n} {len(queries)}\n"
    for l, r, a in queries:
        input_data += f"{l} {r} {a}\n"
    
    try:
        result = subprocess.run(
            ['python3', 'w.py'],
            input=input_data,
            capture_output=True,
            text=True,
            timeout=5
        )
        
        output = result.stdout.strip()
        actual = int(output)
        return actual == expected, actual
    except Exception as e:
        return False, str(e)

# Test cases
tests = [
    # (n, queries, expected, description)
    (1, [(1, 1, 10)], 10, "Single query, single position"),
    (2, [(1, 1, 5), (2, 2, 5)], 10, "Two non-overlapping queries"),
    (2, [(1, 1, 5), (1, 2, 5)], 10, "Overlapping queries"),
    (3, [(1, 3, 100), (1, 1, -10), (2, 2, -20), (3, 3, -30)], 90, "Mixed"),
    (1, [(1, 1, 1000000000)] * 5, 5000000000, "Five identical queries"),
    (6, [(5, 5, 3), (1, 1, 10), (1, 6, -8), (3, 6, 5), (3, 4, 9), (5, 5, -2), (1, 3, -6), (4, 6, -7)], 10, "Complex"),
    
    # Edge cases
    (1, [(1, 1, -100)], 0, "Single negative"),
    (2, [(1, 1, -10), (2, 2, -20)], 0, "All negative"),
    (3, [(1, 1, 100), (2, 2, 200), (3, 3, 300)], 600, "Three independent"),
    (3, [(1, 3, 100)], 100, "Single spanning all"),
    (5, [(1, 3, 50), (2, 4, 50), (3, 5, 50)], 150, "Overlapping ranges"),
]

print("Running tests for Problem W...\n")
passed = 0
failed = 0

for n, queries, expected, description in tests:
    success, actual = run_test(n, queries, expected)
    
    if success:
        print(f"✓ PASS: {description}")
        print(f"  n={n}, queries={len(queries)}, result={actual}")
        passed += 1
    else:
        print(f"✗ FAIL: {description}")
        print(f"  n={n}, queries={len(queries)}, expected={expected}, actual={actual}")
        failed += 1
    print()

print(f"\n{'='*60}")
print(f"Results: {passed} passed, {failed} failed")

if failed == 0:
    print("\n✓ All tests passed!")
else:
    sys.exit(1)
