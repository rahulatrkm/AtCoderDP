# AtCoder DP Contest Solutions

Dynamic Programming practice problems from [AtCoder Educational DP Contest](https://atcoder.jp/contests/dp).

## Problems

### Problem A: Frog 1
**Problem Link:** https://atcoder.jp/contests/dp/tasks/dp_a

#### Problem Statement
There are N stones numbered 1 to N. For each stone i, its height is h_i.

A frog starts at stone 1 and wants to reach stone N. From stone i, the frog can:
- Jump to stone i+1 with cost |h_i - h_{i+1}|
- Jump to stone i+2 with cost |h_i - h_{i+2}|

Find the minimum total cost to reach stone N.

#### Constraints
- 2 ≤ N ≤ 10^5
- 1 ≤ h_i ≤ 10^4

#### Solution Approach
**Dynamic Programming**

- **State:** `dp[i]` = minimum cost to reach stone i
- **Base Case:** `dp[0] = 0` (starting position, no cost)
- **Transition:** `dp[i] = min(dp[i-1] + |h[i] - h[i-1]|, dp[i-2] + |h[i] - h[i-2]|)`
- **Answer:** `dp[n-1]`

#### Complexity Analysis
- **Time Complexity:** O(N) - single pass through all stones
- **Space Complexity:** O(N) - DP array storage

---

### Problem B: Frog 2
**Problem Link:** https://atcoder.jp/contests/dp/tasks/dp_b

#### Problem Statement
There are N stones numbered 1 to N. For each stone i, its height is h_i.

A frog starts at stone 1 and wants to reach stone N. From stone i, the frog can:
- Jump to any stone from i+1, i+2, ..., i+K with cost |h_i - h_j| where j is the landing stone

Find the minimum total cost to reach stone N.

#### Constraints
- 2 ≤ N ≤ 10^5
- 1 ≤ K ≤ 100
- 1 ≤ h_i ≤ 10^4

#### Solution Approach
**Dynamic Programming (Generalized)**

- **State:** `dp[i]` = minimum cost to reach stone i
- **Base Case:** `dp[0] = 0` (starting position, no cost)
- **Transition:** `dp[i] = min(dp[i-j] + |h[i] - h[i-j]|)` for all j from 1 to min(K, i)
- **Answer:** `dp[n-1]`

#### Complexity Analysis
- **Time Complexity:** O(N × K) - for each stone, check up to K previous stones
- **Space Complexity:** O(N) - DP array storage

#### Implementation Details
```python
def frog_jump_cost(n, k, heights):
    dp = [float('inf')] * n
    dp[0] = 0
    
    for i in range(1, n):
        for j in range(1, min(k, i) + 1):
            dp[i] = min(dp[i], dp[i-j] + abs(heights[i] - heights[i-j]))
    
    return dp[-1]
```

## Running the Code

### Prerequisites
- Python 3.6 or higher

### Execution
```bash
# Problem A: Frog 1
python3 a.py

# Problem B: Frog 2
python3 b.py
```

## Test Cases

Both solutions include comprehensive test cases covering:

### Official AtCoder Samples
**Problem A (Frog 1):**
- ✅ Sample 1: Basic test case (Expected: 30)
- ✅ Sample 2: Same heights (Expected: 0)
- ✅ Sample 3: Complex path selection (Expected: 40)

**Problem B (Frog 2):**
- ✅ Sample 1: n=5, k=3 (Expected: 30)
- ✅ Sample 2: n=3, k=1 (Expected: 20)
- ✅ Sample 3: n=2, k=100 (Expected: 0)
- ✅ Sample 4: n=10, k=4 (Expected: 40)

### Edge Cases
**Common Edge Cases:**
1. **All same heights** - Verifies zero cost when no height difference
2. **Strictly increasing** - Tests monotonic increase pattern
3. **Strictly decreasing** - Tests monotonic decrease pattern
4. **Maximum height differences** - Tests with constraint limits (h ≤ 10^4)
5. **Minimum N=2** - Boundary case testing
6. **Large N (1000, 10000)** - Performance testing near constraint limit
7. **Zigzag pattern** - Tests complex oscillating heights
8. **Valley pattern** - Tests downhill-uphill scenarios
9. **Peak pattern** - Tests uphill-downhill scenarios
10. **Alternating pattern** - Tests optimal jump selection

**Problem B Specific Edge Cases:**
- **k=1** - Only one step at a time (reduces to Problem A variant)
- **k >> n** - When k is much larger than n (direct jump possible)
- **k at max constraint (100)** - Boundary testing
- **Various k values comparison** - Shows how larger k enables better paths
- **Flat with spike** - Tests obstacle skipping with different k values

### Sample Output
```
=== AtCoder Sample Test Cases ===
Sample 1 (n=5, k=3): 30 (Expected: 30)
Sample 2 (n=3, k=1): 20 (Expected: 20)
Sample 3 (n=2, k=100): 0 (Expected: 0)
Sample 4 (n=10, k=4): 40 (Expected: 40)

=== Additional Test Cases ===
Edge Case 1 - k=1 (n=10, k=1): 9 (Expected: 9)
Edge Case 2 - Direct jump possible (n=5, k=4): 99 (Expected: 99, Path: 1->5)
...
✅ All test cases completed!
```

## Project Structure
```
AtCoderDP/
├── README.md          # This file
├── a.py              # Problem A: Frog 1 solution with test cases
├── b.py              # Problem B: Frog 2 solution with test cases
└── .gitignore        # Git ignore file
```

## Problems Progress
- ✅ **Problem A: Frog 1** - Complete with comprehensive tests
- ✅ **Problem B: Frog 2** - Complete with comprehensive tests
- ⏳ **Problem C: Vacation** - Coming soon
- ⏳ **Problem D: Knapsack 1** - Coming soon
- ⏳ More problems to be added...

## Author
**Rahul** - [GitHub Profile](https://github.com/rahulatrkm)

## License
This project is open source and available for educational purposes.

## Acknowledgments
- [AtCoder](https://atcoder.jp/) for providing excellent DP practice problems
- Educational DP Contest for structured learning path

---
⭐ Star this repository if you find it helpful!
