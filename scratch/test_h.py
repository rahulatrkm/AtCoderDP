'''
Comprehensive test for Problem H - Grid Paths
Constraints: H, W ≤ 1000, count paths from (0,0) to (H-1,W-1), avoid '#'
Tests edge cases, time and space complexity
'''

import subprocess
import time

def run_test(h, w, grid, expected, description, timeout=5):
    """Run test and measure time"""
    input_str = f"{h} {w}\n"
    input_str += "\n".join(grid)
    
    try:
        start = time.time()
        result = subprocess.run(
            ['python3', 'h.py'],
            input=input_str,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        elapsed = time.time() - start
        
        if result.returncode != 0:
            print(f"✗ {description}: CRASHED")
            print(f"   Error: {result.stderr[:200]}")
            return False
        
        output = int(result.stdout.strip())
        passed = output == expected
        status = "✓" if passed else "✗"
        time_icon = "⚡" if elapsed < 0.5 else "🐌" if elapsed > 2 else "⏱️"
        
        print(f"{status} {time_icon} {description}")
        print(f"   Result: {output} (Expected: {expected}) [{elapsed:.3f}s]")
        return passed
        
    except subprocess.TimeoutExpired:
        print(f"✗ ⏰ {description}: TIMEOUT (>{timeout}s)")
        return False
    except Exception as e:
        print(f"✗ ❌ {description}: ERROR - {str(e)}")
        return False

print("="*80)
print("PROBLEM H: Grid Paths (Count paths with obstacles)")
print("Constraints: H, W ≤ 1000, mod 10^9+7")
print("="*80)

passed = 0
total = 0

# Sample tests
print("\n[Sample Tests]")
total += 1
sample1 = [
    "...",
    ".#.",
    "..."
]
passed += run_test(3, 3, sample1, 2, "Sample 1: 3x3 with obstacle")

total += 1
sample2 = [
    "....",
    ".#..",
    "..#.",
    "...."
]
passed += run_test(4, 4, sample2, 4, "Sample 2: 4x4 with obstacles")

# Edge cases
print("\n[Edge Cases]")
total += 1
passed += run_test(1, 1, ["."], 1, "1x1 grid")

total += 1
passed += run_test(2, 2, ["..", ".."], 2, "2x2 no obstacles")

total += 1
passed += run_test(2, 2, [".#", ".."], 1, "2x2 top-right blocked")

total += 1
passed += run_test(2, 2, ["..", ".#"], 0, "2x2 end blocked")

total += 1
passed += run_test(1, 5, ["....."], 1, "1x5 single row")

total += 1
passed += run_test(5, 1, [".", ".", ".", ".", "."], 1, "5x1 single column")

total += 1
passed += run_test(3, 3, ["...", "###", "..."], 0, "3x3 no path (wall)")

# Rectangular grids
print("\n[Rectangular Grids]")
total += 1
passed += run_test(2, 5, [".....", "....."], 5, "2x5 no obstacles")

total += 1
passed += run_test(5, 2, ["..", "..", "..", "..", ".."], 5, "5x2 no obstacles")

total += 1
passed += run_test(3, 4, ["....", "....", "...."], 10, "3x4 no obstacles")

# Large grids with no obstacles (combinatorics)
print("\n[Large Grids - Combinatorics]")
total += 1
grid_10x10 = ["."*10 for _ in range(10)]
# Paths = C(18, 9) = 48620
passed += run_test(10, 10, grid_10x10, 48620, "10x10 no obstacles")

total += 1
grid_20x20 = ["."*20 for _ in range(20)]
# Paths = C(38, 19) mod (10^9+7)
passed += run_test(20, 20, grid_20x20, 345263555, "20x20 no obstacles")

# Zigzag obstacles
print("\n[Complex Obstacle Patterns]")
total += 1
zigzag = [
    ".....",
    ".#...",
    "..#..",
    "...#.",
    "....."
]
passed += run_test(5, 5, zigzag, 10, "5x5 zigzag obstacles")

total += 1
checkerboard = [
    ".#.#.",
    "#.#.#",
    ".#.#.",
    "#.#.#",
    ".#.#."
]
passed += run_test(5, 5, checkerboard, 0, "5x5 checkerboard (no path)")

total += 1
corridor = [
    "...........",
    ".#########.",
    "...........",
]
passed += run_test(3, 11, corridor, 2, "3x11 narrow corridor")

# Performance tests
print("\n[Performance Tests - Time & Space]")

# Test 1: Large grid no obstacles
total += 1
grid_100 = ["."*100 for _ in range(100)]
passed += run_test(100, 100, grid_100, 690285631, "100x100 no obstacles", timeout=3)

# Test 2: Large grid with diagonal obstacles
total += 1
grid_100_diag = []
for i in range(100):
    row = ["."] * 100
    if i < 99:
        row[i] = "#"
    grid_100_diag.append("".join(row))
passed += run_test(100, 100, grid_100_diag, 155788253, "100x100 diagonal obstacles", timeout=3)

# Test 3: Large grid mostly blocked
total += 1
grid_100_blocked = []
for i in range(100):
    row = ["."] * 100
    for j in range(1, 99):
        if (i + j) % 3 == 0:
            row[j] = "#"
    grid_100_blocked.append("".join(row))
passed += run_test(100, 100, grid_100_blocked, 0, "100x100 many obstacles (blocks path)", timeout=3)

# Test 4: Maximum constraints
print("\n⚠️  Maximum constraint tests:")
total += 1
grid_500 = ["."*500 for _ in range(500)]
passed += run_test(500, 500, grid_500, 264223182, "500x500 no obstacles", timeout=5)

total += 1
grid_1000 = ["."*1000 for _ in range(1000)]
passed += run_test(1000, 1000, grid_1000, 965601742, "1000x1000 no obstacles (MAX)", timeout=10)

# Test 5: Rectangular max
total += 1
grid_1000x100 = ["."*100 for _ in range(1000)]
passed += run_test(1000, 100, grid_1000x100, 376063885, "1000x100 rectangular", timeout=5)

# Summary
print("\n" + "="*80)
print("SUMMARY")
print("="*80)
print(f"Tests Passed: {passed}/{total}")
print(f"\nComplexity Analysis:")
print(f"  Time: O(H × W) - Fill DP table")
print(f"  Space: O(H × W) - DP table (can optimize to O(W))")
print(f"  Max: H=1000, W=1000 = 1M cells (manageable)")
print(f"  Modulo: 10^9 + 7 for large path counts")
print("="*80)
