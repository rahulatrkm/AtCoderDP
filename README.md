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

#### Implementation Details
```python
def frog_jump_cost(n, heights):
    dp = [float('inf')] * n
    dp[0] = 0
    dp[1] = abs(heights[1] - heights[0])
    
    for i in range(2, n):
        dp[i] = min(
            dp[i-1] + abs(heights[i-1] - heights[i]),
            dp[i-2] + abs(heights[i-2] - heights[i])
        )
    
    return dp[-1]
```

## Running the Code

### Prerequisites
- Python 3.6 or higher

### Execution
```bash
python3 a.py
```

## Test Cases

The solution includes comprehensive test cases covering:

### Official AtCoder Samples
- ✅ Sample 1: Basic test case (Expected: 30)
- ✅ Sample 2: Same heights (Expected: 0)
- ✅ Sample 3: Complex path selection (Expected: 40)

### Edge Cases
1. **All same heights** - Verifies zero cost when no height difference
2. **Strictly increasing** - Tests monotonic increase pattern
3. **Strictly decreasing** - Tests monotonic decrease pattern
4. **Alternating pattern** - Tests optimal jump selection
5. **Maximum height differences** - Tests with constraint limits (h ≤ 10^4)
6. **Minimum N=2** - Boundary case testing
7. **Large N (1000, 10000)** - Performance testing near constraint limit
8. **Zigzag pattern** - Tests complex oscillating heights
9. **Valley pattern** - Tests downhill-uphill scenarios
10. **Peak pattern** - Tests uphill-downhill scenarios
11. **Random large arrays** - Stress testing with varied data

### Sample Output
```
=== AtCoder Sample Test Cases ===
Sample 1 (n=4): 30 (Expected: 30)
Sample 2 (n=2): 0 (Expected: 0)
Sample 3 (n=6): 40 (Expected: 40)

=== Additional Test Cases ===
...
✅ All test cases completed!
```

## Project Structure
```
AtCoderDP/
├── README.md          # This file
├── a.py              # Problem A: Frog 1 solution
└── .gitignore        # Git ignore file
```

## Future Problems
More DP problems from the contest will be added:
- Problem B: Frog 2
- Problem C: Vacation
- Problem D: Knapsack 1
- And more...

## Author
**Rahul** - [GitHub Profile](https://github.com/rahulatrkm)

## License
This project is open source and available for educational purposes.

## Acknowledgments
- [AtCoder](https://atcoder.jp/) for providing excellent DP practice problems
- Educational DP Contest for structured learning path

---
⭐ Star this repository if you find it helpful!
