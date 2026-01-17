'''
Test suite for Problem C: Vacation
Tests the original c.py implementation with comprehensive edge cases
'''

import subprocess

def run_test(n, activities, expected, description):
    """Run c.py with given input and check output"""
    input_str = f"{n}\n"
    for a, b, c in activities:
        input_str += f"{a} {b} {c}\n"
    
    result = subprocess.run(
        ['python3', 'c.py'],
        input=input_str,
        capture_output=True,
        text=True,
        cwd='/Users/rahul./Downloads/AtCoderDP'
    )
    
    output = int(result.stdout.strip())
    status = "✓" if output == expected else "✗"
    print(f"{status} {description}: {output} (Expected: {expected})")
    return output == expected

print("=== AtCoder Sample Test Cases ===")
all_pass = True

# Sample 1
all_pass &= run_test(3, [(10, 40, 70), (20, 50, 80), (30, 60, 90)], 210, "Sample 1 (n=3)")

# Sample 2
all_pass &= run_test(1, [(100, 10, 1)], 100, "Sample 2 (n=1)")

# Sample 3
all_pass &= run_test(7, [(6, 7, 8), (8, 8, 3), (2, 5, 2), (7, 8, 6), (4, 6, 8), (2, 3, 4), (7, 5, 1)], 46, "Sample 3 (n=7)")

print("\n=== Edge Cases ===")

# Edge Case 1: All activities have same points
all_pass &= run_test(3, [(10, 10, 10), (20, 20, 20), (30, 30, 30)], 60, "Edge 1: All same values")

# Edge Case 2: One activity always best (must alternate)
all_pass &= run_test(4, [(100, 1, 1), (100, 1, 1), (100, 1, 1), (100, 1, 1)], 202, "Edge 2: One dominant activity")

# Edge Case 3: Strictly increasing
all_pass &= run_test(4, [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)], 28, "Edge 3: Strictly increasing")

# Edge Case 4: Alternating best choice
all_pass &= run_test(4, [(100, 1, 1), (1, 100, 1), (100, 1, 1), (1, 100, 1)], 400, "Edge 4: Alternating best")

# Edge Case 5: Maximum values at constraint
all_pass &= run_test(3, [(10000, 10000, 10000), (10000, 10000, 10000), (10000, 10000, 10000)], 30000, "Edge 5: Max values 10^4")

# Edge Case 6: Minimum n=1, best C
all_pass &= run_test(1, [(1, 2, 3)], 3, "Edge 6: Min n=1, best C")

# Edge Case 7: Minimum n=1, best A
all_pass &= run_test(1, [(100, 50, 25)], 100, "Edge 7: Min n=1, best A")

# Edge Case 8: Large n=100
activities = [(i % 10 + 1, i % 10 + 2, i % 10 + 3) for i in range(100)]
all_pass &= run_test(100, activities, 700, "Edge 8: Large n=100")

# Edge Case 9: Zigzag A-B
all_pass &= run_test(5, [(100, 50, 1), (50, 100, 1), (100, 50, 1), (50, 100, 1), (100, 50, 1)], 500, "Edge 9: Zigzag A-B")

# Edge Case 10: All zeros
all_pass &= run_test(3, [(0, 0, 0), (0, 0, 0), (0, 0, 0)], 0, "Edge 10: All zeros")

# Edge Case 11: One activity always worst
all_pass &= run_test(4, [(100, 100, 1), (100, 100, 1), (100, 100, 1), (100, 100, 1)], 400, "Edge 11: One always worst")

# Edge Case 12: Decreasing pattern
all_pass &= run_test(4, [(100, 90, 80), (70, 60, 50), (40, 30, 20), (10, 5, 1)], 205, "Edge 12: Decreasing")

# Edge Case 13: Activity A always 0
all_pass &= run_test(4, [(0, 50, 100), (0, 60, 110), (0, 70, 120), (0, 80, 130)], 360, "Edge 13: Activity A always 0")

# Edge Case 14: Large n=1000
activities = [(i % 100 + 1, (i + 1) % 100 + 1, (i + 2) % 100 + 1) for i in range(1000)]
all_pass &= run_test(1000, activities, 51980, "Edge 14: Large n=1000")

# Edge Case 15: Middle activity always best
all_pass &= run_test(4, [(10, 100, 10), (10, 100, 10), (10, 100, 10), (10, 100, 10)], 220, "Edge 15: Middle always best")

# Edge Case 16: Last activity always best
all_pass &= run_test(4, [(10, 20, 100), (10, 20, 100), (10, 20, 100), (10, 20, 100)], 240, "Edge 16: Last always best")

# Edge Case 17: Random pattern
all_pass &= run_test(5, [(45, 78, 12), (67, 23, 89), (34, 90, 56), (12, 45, 78), (89, 34, 23)], 424, "Edge 17: Random pattern")

# Edge Case 18: Extreme differences
all_pass &= run_test(5, [(10000, 1, 1), (1, 10000, 1), (1, 1, 10000), (10000, 1, 1), (1, 10000, 1)], 50000, "Edge 18: Extreme differences")

# Edge Case 19: Valley pattern
all_pass &= run_test(7, [(100, 80, 60), (80, 60, 40), (60, 40, 20), (40, 20, 10), (60, 40, 20), (80, 60, 40), (100, 80, 60)], 460, "Edge 19: Valley pattern")

# Edge Case 20: Two activities close in value
all_pass &= run_test(3, [(50, 51, 10), (50, 51, 10), (50, 51, 10)], 152, "Edge 20: Close values")

print("\n" + "="*50)
if all_pass:
    print("✅ All test cases PASSED!")
else:
    print("❌ Some test cases FAILED!")
print("="*50)
