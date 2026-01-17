'''
REFERENCE SOLUTION for Problem E: Knapsack 2
This is the CORRECT approach for when W can be up to 10^9

Key insight: DP on VALUES instead of WEIGHTS
'''

def knapsack_2_correct(n, w, items):
    """
    Correct solution for Knapsack 2 (large W, small values)
    
    dp[v] = minimum weight needed to achieve exactly value v
    
    Time: O(N * sum_of_values) = O(100 * 100,000) = O(10^7) ✓
    Memory: O(sum_of_values) = O(100,000) ✓
    """
    # Maximum possible value
    max_value = sum(v for w, v in items)
    
    # dp[v] = minimum weight to achieve value v
    INF = float('inf')
    dp = [INF] * (max_value + 1)
    dp[0] = 0  # 0 weight for 0 value
    
    # Process each item
    for item_weight, item_value in items:
        # Traverse backwards to avoid using same item twice
        for v in range(max_value, item_value - 1, -1):
            if dp[v - item_value] != INF:
                dp[v] = min(dp[v], dp[v - item_value] + item_weight)
    
    # Find maximum value where weight <= W
    result = 0
    for v in range(max_value + 1):
        if dp[v] <= w:
            result = v
    
    return result


# Example usage:
if __name__ == "__main__":
    # Sample 1: Works with both approaches
    print("Sample 1:", knapsack_2_correct(3, 8, [(3, 30), (4, 50), (5, 60)]))
    # Output: 90
    
    # Sample 2: Only works with dp on values!
    print("Sample 2:", knapsack_2_correct(1, 1000000000, [(1000000000, 10)]))
    # Output: 10
    
    # Sample 3
    print("Sample 3:", knapsack_2_correct(6, 15, [(6, 5), (5, 6), (6, 4), (6, 6), (3, 5), (7, 2)]))
    # Output: 17
    
    # Large W test - this would crash with dp[W] approach
    print("Large W test:", knapsack_2_correct(3, 10**9, [(100, 50), (200, 100), (300, 150)]))
    # Output: 300
