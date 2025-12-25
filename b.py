'''
ps - https://atcoder.jp/contests/dp/tasks/dp_b
'''

def frog_jump_cost(n, k, heights):
    dp = [float('inf')]*n
    dp[0] = 0
    for i in range(1, n):
        for j in range(1, min(k, i)+1):
            dp[i] = min(dp[i], dp[i-j] + abs(heights[i] - heights[i-j]))
    return dp[-1]

# Original AtCoder Sample Test Cases
print("=== AtCoder Sample Test Cases ===")
n = 5
k = 3
ht = [10, 30, 40, 50, 20]
print(f"Sample 1 (n={n}, k={k}): {frog_jump_cost(n, k, ht)} (Expected: 30)")

n = 3
k = 1
ht = [10, 20, 10]
print(f"Sample 2 (n={n}, k={k}): {frog_jump_cost(n, k, ht)} (Expected: 20)")

n = 2
k = 100
ht = [10, 10]
print(f"Sample 3 (n={n}, k={k}): {frog_jump_cost(n, k, ht)} (Expected: 0)")

n = 10
k = 4
ht = [40, 10, 20, 70, 80, 10, 20, 70, 80, 60]
print(f"Sample 4 (n={n}, k={k}): {frog_jump_cost(n, k, ht)} (Expected: 40)")

print("\n=== Additional Test Cases ===")

# Edge Case 1: k = 1 (only one step at a time, like climbing stairs)
n = 10
k = 1
ht = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Edge Case 1 - k=1 (n={n}, k={k}): {frog_jump_cost(n, k, ht)} (Expected: 9)")

# Edge Case 2: k = n-1 (can jump directly to end)
n = 5
k = 4
ht = [100, 1, 2, 3, 1]
result = frog_jump_cost(n, k, ht)
print(f"Edge Case 2 - Direct jump possible (n={n}, k={k}): {result} (Expected: 99, Path: 1->5)")

# Edge Case 3: All same heights
n = 10
k = 5
ht = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]
print(f"Edge Case 3 - All same heights (n={n}, k={k}): {frog_jump_cost(n, k, ht)} (Expected: 0)")

# Edge Case 4: k >> n (k much larger than n)
n = 5
k = 100
ht = [10, 20, 30, 40, 50]
result = frog_jump_cost(n, k, ht)
print(f"Edge Case 4 - k >> n (n={n}, k={k}): {result} (Expected: 40, Path: 1->5)")

# Edge Case 5: Strictly increasing heights
n = 10
k = 3
ht = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Edge Case 5 - Strictly increasing (n={n}, k={k}): {frog_jump_cost(n, k, ht)}")

# Edge Case 6: Strictly decreasing heights
n = 10
k = 3
ht = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
print(f"Edge Case 6 - Strictly decreasing (n={n}, k={k}): {frog_jump_cost(n, k, ht)}")

# Edge Case 7: Minimum n = 2, k = 1
n = 2
k = 1
ht = [1, 10000]
print(f"Edge Case 7 - Min n=2, k=1, max diff (n={n}, k={k}): {frog_jump_cost(n, k, ht)} (Expected: 9999)")

# Edge Case 8: Alternating high-low with different k values
n = 10
k = 2
ht = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100]
print(f"Edge Case 8 - Alternating k=2 (n={n}, k={k}): {frog_jump_cost(n, k, ht)}")

n = 10
k = 5
ht = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100]
print(f"Edge Case 8b - Alternating k=5 (n={n}, k={k}): {frog_jump_cost(n, k, ht)}")

# Edge Case 9: Valley pattern with different k
n = 7
k = 2
ht = [100, 80, 60, 40, 60, 80, 100]
print(f"Edge Case 9 - Valley k=2 (n={n}, k={k}): {frog_jump_cost(n, k, ht)}")

n = 7
k = 4
ht = [100, 80, 60, 40, 60, 80, 100]
print(f"Edge Case 9b - Valley k=4 (n={n}, k={k}): {frog_jump_cost(n, k, ht)}")

# Edge Case 10: Peak pattern with different k
n = 7
k = 2
ht = [40, 60, 80, 100, 80, 60, 40]
print(f"Edge Case 10 - Peak k=2 (n={n}, k={k}): {frog_jump_cost(n, k, ht)}")

n = 7
k = 4
ht = [40, 60, 80, 100, 80, 60, 40]
print(f"Edge Case 10b - Peak k=4 (n={n}, k={k}): {frog_jump_cost(n, k, ht)}")

# Edge Case 11: Maximum height differences
n = 5
k = 2
ht = [10000, 1, 10000, 1, 10000]
print(f"Edge Case 11 - Max diff k=2 (n={n}, k={k}): {frog_jump_cost(n, k, ht)}")

n = 5
k = 4
ht = [10000, 1, 10000, 1, 10000]
print(f"Edge Case 11b - Max diff k=4 (n={n}, k={k}): {frog_jump_cost(n, k, ht)} (Expected: 0, Path: 1->5)")

# Edge Case 12: Large k means optimal path is just max jumps
n = 10
k = 9
ht = [10, 5, 15, 3, 20, 8, 25, 12, 30, 1]
print(f"Edge Case 12 - Large k=9 (n={n}, k={k}): {frog_jump_cost(n, k, ht)}")

# Edge Case 13: Zigzag pattern with different k
n = 8
k = 3
ht = [10, 20, 15, 25, 20, 30, 25, 35]
print(f"Edge Case 13 - Zigzag k=3 (n={n}, k={k}): {frog_jump_cost(n, k, ht)}")

# Edge Case 14: Large n with moderate k
n = 100
k = 5
ht = [i % 50 for i in range(100)]
print(f"Edge Case 14 - Large n=100, k=5: {frog_jump_cost(n, k, ht)}")

# Edge Case 15: Large n approaching constraint
n = 1000
k = 10
ht = [(i * 7 + 13) % 100 + 1 for i in range(1000)]
print(f"Edge Case 15 - Large n=1000, k=10: {frog_jump_cost(n, k, ht)}")

# Edge Case 16: k at max constraint (K ≤ 100)
n = 100
k = 100
ht = [i * 2 for i in range(100)]
result = frog_jump_cost(n, k, ht)
print(f"Edge Case 16 - Max k=100 (n={n}, k={k}): {result} (Expected: 198, Path: 1->100)")

# Edge Case 17: Flat with spike - test if skipping is better
n = 6
k = 2
ht = [10, 10, 10, 10000, 10, 10]
print(f"Edge Case 17 - Flat with spike k=2 (n={n}, k={k}): {frog_jump_cost(n, k, ht)} (Expected: 0)")

n = 6
k = 4
ht = [10, 10, 10, 10000, 10, 10]
print(f"Edge Case 17b - Flat with spike k=4 (n={n}, k={k}): {frog_jump_cost(n, k, ht)} (Expected: 0)")

print("\n✅ All test cases completed!")