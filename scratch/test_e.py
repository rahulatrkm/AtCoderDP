'''
Test suite for Problem E: Knapsack 2
Tests edge cases and checks time/memory constraints

IMPORTANT: Problem E requires DP on VALUES (not weights) because:
- W can be up to 10^9 (would cause memory error with dp[W+1])
- v_i can be at most 10^3, and N ≤ 100
- Max total value = 100 * 1000 = 100,000
- So we need dp[100001] instead of dp[10^9+1]

Current code in e.py will FAIL for large W (W > 10^7 approx) due to memory constraints!
'''

import subprocess
import time
import sys

def run_test(n, w, items, expected, description, should_fail=False):
    """Run e.py with given input and check output"""
    input_str = f"{n} {w}\n"
    for item_w, item_v in items:
        input_str += f"{item_w} {item_v}\n"
    
    try:
        start_time = time.time()
        result = subprocess.run(
            ['python3', 'e.py'],
            input=input_str,
            capture_output=True,
            text=True,
            cwd='/Users/rahul./Downloads/AtCoderDP',
            timeout=3  # 3 second timeout
        )
        elapsed = time.time() - start_time
        
        if result.returncode != 0:
            print(f"✗ {description}: CRASHED (probably MemoryError for large W)")
            return False
        
        output = int(result.stdout.strip())
        status = "✓" if output == expected else "✗"
        time_str = f"({elapsed:.3f}s)"
        print(f"{status} {description}: {output} (Expected: {expected}) {time_str}")
        return output == expected
    except subprocess.TimeoutExpired:
        print(f"✗ {description}: TIMEOUT (>3s) - algorithm too slow")
        return False
    except Exception as e:
        print(f"✗ {description}: ERROR - {str(e)}")
        return False

print("=== AtCoder Sample Test Cases ===")
all_pass = True

# Sample 1
all_pass &= run_test(3, 8, [(3, 30), (4, 50), (5, 60)], 90, "Sample 1 (n=3, W=8)")

# Sample 2 - THIS WILL LIKELY FAIL due to W=10^9
print("\n⚠️  WARNING: Sample 2 has W=10^9 - current code will likely crash with MemoryError")
all_pass &= run_test(1, 1000000000, [(1000000000, 10)], 10, "Sample 2 (W=10^9) - EXPECTED TO FAIL")

# Sample 3
all_pass &= run_test(6, 15, [(6, 5), (5, 6), (6, 4), (6, 6), (3, 5), (7, 2)], 17, "Sample 3 (n=6, W=15)")

print("\n=== Small W Edge Cases (These should work) ===")

# Edge Case 1: Single item
all_pass &= run_test(1, 10, [(5, 100)], 100, "Edge 1: Single item fits")

# Edge Case 2: Single item doesn't fit
all_pass &= run_test(1, 10, [(15, 100)], 0, "Edge 2: Single item doesn't fit")

# Edge Case 3: Max values v_i = 1000
all_pass &= run_test(3, 10, [(3, 1000), (4, 1000), (5, 1000)], 2000, "Edge 3: Max values v=1000")

# Edge Case 4: All items weight 1
all_pass &= run_test(5, 5, [(1, 100), (1, 200), (1, 300), (1, 400), (1, 500)], 1500, "Edge 4: All weight 1")

# Edge Case 5: W=1 (minimum)
all_pass &= run_test(3, 1, [(1, 100), (2, 200), (3, 300)], 100, "Edge 5: Min W=1")

# Edge Case 6: Maximum N=100
items = [(i % 10 + 1, (i + 1) * 10) for i in range(100)]
all_pass &= run_test(100, 1000, items, 50500, "Edge 6: Max N=100")

print("\n=== Large W Edge Cases (These will FAIL with current approach) ===")
print("⚠️  Current code uses dp[W+1] which causes MemoryError for large W")

# Edge Case 7: W=10^7
all_pass &= run_test(3, 10000000, [(100, 50), (200, 100), (300, 150)], 300, "Edge 7: W=10^7 (will crash)")

# Edge Case 8: W=10^8
all_pass &= run_test(2, 100000000, [(1000, 100), (2000, 200)], 300, "Edge 8: W=10^8 (will crash)")

# Edge Case 9: W=10^9 (maximum)
all_pass &= run_test(1, 1000000000, [(500000000, 500)], 1000, "Edge 9: W=10^9 max (will crash)")

print("\n=== Performance Analysis ===")
print("Current approach: dp[W+1] array")
print("  Memory: O(W) - FAILS when W > 10^7 (approx)")
print("  Time: O(N * W)")
print()
print("REQUIRED approach for this problem: dp[VALUE] array")
print("  Memory: O(N * max_value) = O(100 * 1000) = O(100,000) ✓")
print("  Time: O(N * N * max_value) = O(100 * 100 * 1000) = O(10^7) ✓")
print()
print("Max total value = N * max(v_i) = 100 * 1000 = 100,000")
print("So dp array should be: dp[100001] (always safe)")
print()
print("Algorithm: For each total value V, find minimum weight needed")
print("  dp[v] = minimum weight to achieve value v")
print("  Answer = max v where dp[v] <= W")

print("\n" + "="*60)
if all_pass:
    print("✅ All test cases PASSED!")
else:
    print("❌ Some test cases FAILED!")
    print("\n⚠️  CRITICAL: Current code will fail for W > 10^7")
    print("   Need to change approach: DP on VALUES instead of WEIGHTS")
print("="*60)
