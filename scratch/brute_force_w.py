"""
Brute force solution to verify correct answer
"""

def brute_force(n, queries):
    max_score = 0
    # Try all 2^n possible configurations
    for mask in range(1 << n):
        config = [(mask >> i) & 1 for i in range(n)]
        score = 0
        for l, r, a in queries:
            # Check if there's at least one '1' in [l, r]
            if any(config[i] == 1 for i in range(l, r + 1)):
                score += a
        max_score = max(max_score, score)
        if score == max_score:
            best_config = ''.join(map(str, config))
    return max_score

# Test case 1
n1 = 3
queries1 = [(0, 2, 100), (0, 0, -10), (1, 1, -20), (2, 2, -30)]
result1 = brute_force(n1, queries1)
print(f"Test 1: {result1}")

# Test case 2
n2 = 5
queries2 = [(0, 2, 10), (1, 3, -10), (2, 4, 10)]
result2 = brute_force(n2, queries2)
print(f"Test 2: {result2}")
