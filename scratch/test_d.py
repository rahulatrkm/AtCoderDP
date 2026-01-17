'''
Test suite for Problem D: Knapsack 1
Tests the original d.py implementation with comprehensive edge cases
'''

import subprocess

def run_test(n, w, items, expected, description):
    """Run d.py with given input and check output"""
    input_str = f"{n} {w}\n"
    for item_w, item_v in items:
        input_str += f"{item_w} {item_v}\n"
    
    result = subprocess.run(
        ['python3', 'd.py'],
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
all_pass &= run_test(3, 8, [(3, 30), (4, 50), (5, 60)], 90, "Sample 1 (n=3, W=8)")

# Sample 2
all_pass &= run_test(5, 5, [(1, 1000000000)] * 5, 5000000000, "Sample 2 (n=5, W=5, large values)")

# Sample 3
all_pass &= run_test(6, 15, [(6, 5), (5, 6), (6, 4), (6, 6), (3, 5), (7, 2)], 17, "Sample 3 (n=6, W=15)")

print("\n=== Edge Cases ===")

# Edge Case 1: Single item that fits
all_pass &= run_test(1, 10, [(5, 100)], 100, "Edge 1: Single item fits")

# Edge Case 2: Single item doesn't fit
all_pass &= run_test(1, 10, [(15, 100)], 0, "Edge 2: Single item doesn't fit")

# Edge Case 3: All items = capacity (can only take one)
all_pass &= run_test(3, 10, [(10, 50), (10, 100), (10, 75)], 100, "Edge 3: All items = W")

# Edge Case 4: All items weight 1
all_pass &= run_test(5, 5, [(1, 10), (1, 20), (1, 30), (1, 40), (1, 50)], 150, "Edge 4: All weight 1")

# Edge Case 5: Minimum capacity W=1
all_pass &= run_test(3, 1, [(1, 100), (2, 200), (3, 300)], 100, "Edge 5: Min capacity W=1")

# Edge Case 6: No items fit
all_pass &= run_test(3, 5, [(10, 100), (20, 200), (30, 300)], 0, "Edge 6: No items fit")

# Edge Case 7: All same value
all_pass &= run_test(4, 10, [(1, 50), (2, 50), (3, 50), (4, 50)], 200, "Edge 7: All same value")

# Edge Case 8: All same weight
all_pass &= run_test(4, 9, [(3, 10), (3, 20), (3, 30), (3, 40)], 90, "Edge 8: All same weight")

# Edge Case 9: Large capacity W=100000
all_pass &= run_test(4, 100000, [(100, 1000), (200, 3000), (300, 5000), (400, 7000)], 16000, "Edge 9: Large W=100000")

# Edge Case 10: Large values v=10^9
all_pass &= run_test(3, 6, [(1, 1000000000), (2, 1000000000), (3, 1000000000)], 3000000000, "Edge 10: Large values v=10^9")

# Edge Case 11: Greedy would fail
all_pass &= run_test(3, 50, [(10, 60), (20, 100), (30, 120)], 220, "Edge 11: Greedy fails")

# Edge Case 12: Take all items
all_pass &= run_test(3, 60, [(10, 100), (20, 200), (30, 300)], 600, "Edge 12: Take all items")

# Edge Case 13: 0/1 constraint (can't split items)
all_pass &= run_test(2, 20, [(10, 100), (15, 90)], 100, "Edge 13: 0/1 constraint")

# Edge Case 14: Reverse value order
all_pass &= run_test(5, 10, [(1, 100), (2, 90), (3, 80), (4, 70), (5, 60)], 340, "Edge 14: Reverse value order")

# Edge Case 15: Last item is best
all_pass &= run_test(4, 10, [(10, 10), (10, 20), (10, 30), (10, 1000)], 1000, "Edge 15: Last item best")

# Edge Case 16: Multiple optimal solutions
all_pass &= run_test(2, 10, [(5, 50), (5, 50)], 100, "Edge 16: Multiple optimal")

# Edge Case 17: Large W with small items
all_pass &= run_test(3, 100000, [(1, 1), (2, 2), (3, 3)], 6, "Edge 17: Large W, small items")

# Edge Case 18: Exact capacity usage
all_pass &= run_test(3, 10, [(2, 20), (3, 30), (5, 50)], 100, "Edge 18: Exact capacity")

# Edge Case 19: Two items with different ratios
all_pass &= run_test(2, 7, [(3, 40), (4, 50)], 90, "Edge 19: Different ratios")

# Edge Case 20: Maximum N=100 items
items = [(i % 10 + 1, (i + 1) * 10) for i in range(100)]
all_pass &= run_test(100, 1000, items, 50500, "Edge 20: Max items N=100")

print("\n" + "="*50)
if all_pass:
    print("✅ All test cases PASSED!")
else:
    print("❌ Some test cases FAILED!")
print("="*50)
