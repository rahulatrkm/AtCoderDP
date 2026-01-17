'''
PS - https://atcoder.jp/contests/dp/tasks/dp_a
'''

def frog_jump_cost(n, heights):
    dp = [float('inf')]*n
    dp[0] = 0
    dp[1] = abs(heights[1] - heights[0])
    for i in range(2, n):
        dp[i] = min(dp[i], dp[i-1] + abs(heights[i-1] - heights[i]), dp[i-2] + abs(heights[i-2] - heights[i]))
    return dp[-1]
    
n = int(input())
ht = list(map(int, input().split()))
print(frog_jump_cost(n, ht))

# Original AtCoder Sample Test Cases
print("=== AtCoder Sample Test Cases ===")
n = 4
ht = [10, 30, 40, 20]
print(f"Sample 1 (n={n}): {frog_jump_cost(n, ht)} (Expected: 30)")

n = 2
ht = [10, 10]
print(f"Sample 2 (n={n}): {frog_jump_cost(n, ht)} (Expected: 0)")

n = 6
ht = [30, 10, 60, 10, 60, 50]
print(f"Sample 3 (n={n}): {frog_jump_cost(n, ht)} (Expected: 40)")

print("\n=== Additional Test Cases ===")

## more test cases
n = 5
ht = [10, 20, 10, 20, 10]
print(f"Test 4 (n={n}): {frog_jump_cost(n, ht)}")

# Edge Case 1: All same heights (minimum cost = 0)
n = 10
ht = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
print(f"\nEdge Case 1 - All same heights (n={n}): {frog_jump_cost(n, ht)} (Expected: 0)")

# Edge Case 2: Strictly increasing heights
n = 10
ht = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Edge Case 2 - Strictly increasing (n={n}): {frog_jump_cost(n, ht)}")

# Edge Case 3: Strictly decreasing heights
n = 10
ht = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
print(f"Edge Case 3 - Strictly decreasing (n={n}): {frog_jump_cost(n, ht)}")

# Edge Case 4: Alternating high-low (jump 2 is mostly better)
n = 10
ht = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100]
print(f"Edge Case 4 - Alternating high-low (n={n}): {frog_jump_cost(n, ht)} (Expected: 99, Path: 0->2->4->6->8->9)")

# Edge Case 5: Maximum height difference - skip middle stones
n = 5
ht = [10000, 1, 10000, 1, 10000]
print(f"Edge Case 5 - Max height diff (n={n}): {frog_jump_cost(n, ht)} (Expected: 0, Path: 0->2->4)")

# Edge Case 6: Minimum n = 2
n = 2
ht = [1, 10000]
print(f"Edge Case 6 - Min n=2, max diff (n={n}): {frog_jump_cost(n, ht)} (Expected: 9999)")

# Edge Case 7: Large n approaching constraint (N ≤ 10^5)
n = 1000
ht = [i % 100 for i in range(1000)]
print(f"Edge Case 7 - Large n=1000: {frog_jump_cost(n, ht)}")

# Edge Case 8: Zigzag pattern
n = 8
ht = [10, 20, 15, 25, 20, 30, 25, 35]
print(f"Edge Case 8 - Zigzag pattern (n={n}): {frog_jump_cost(n, ht)}")

# Edge Case 9: Valley pattern (low in middle)
n = 7
ht = [100, 80, 60, 40, 60, 80, 100]
print(f"Edge Case 9 - Valley pattern (n={n}): {frog_jump_cost(n, ht)}")

# Edge Case 10: Peak pattern (high in middle)
n = 7
ht = [40, 60, 80, 100, 80, 60, 40]
print(f"Edge Case 10 - Peak pattern (n={n}): {frog_jump_cost(n, ht)}")

# Edge Case 11: Two steps mostly optimal
n = 6
ht = [1, 100, 2, 100, 3, 100]
print(f"Edge Case 11 - Two steps optimal (n={n}): {frog_jump_cost(n, ht)} (Expected: 99, Path: 0->2->4->5)")

# Edge Case 12: One step always better (small increments)
n = 10
ht = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(f"Edge Case 12 - One step optimal (n={n}): {frog_jump_cost(n, ht)} (Expected: 9)")

# Edge Case 13: Random large array
n = 100
ht = [56, 23, 78, 12, 45, 67, 89, 34, 23, 90, 12, 34, 56, 78, 90, 21, 43, 65, 87, 32, 54, 76, 98, 11, 22, 33, 44, 55, 66, 77, 88, 99, 10, 20, 30, 40, 50, 60, 70, 80, 90, 15, 25, 35, 45, 55, 65, 75, 85, 95, 14, 24, 34, 44, 54, 64, 74, 84, 94, 13, 23, 33, 43, 53, 63, 73, 83, 93, 12, 22, 32, 42, 52, 62, 72, 82, 92, 11, 21, 31, 41, 51, 61, 71, 81, 91, 10, 19, 29, 39, 49, 59, 69, 79, 89, 99, 18, 28, 38, 48]
print(f"Edge Case 13 - Random n=100: {frog_jump_cost(n, ht)}")

# Edge Case 14: Very large n (10^5)
n = 10000
ht = [(i * 7 + 13) % 10000 + 1 for i in range(10000)]
print(f"Edge Case 14 - Large n=10000: {frog_jump_cost(n, ht)}")

# Edge Case 15: Flat then spike
n = 6
ht = [10, 10, 10, 10000, 10, 10]
print(f"Edge Case 15 - Flat with spike (n={n}): {frog_jump_cost(n, ht)} (Expected: 0)")

print("\n✅ All test cases completed!")

