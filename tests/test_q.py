"""
Test cases for Problem Q: Flowers
https://atcoder.jp/contests/dp/tasks/dp_q
"""

from test_runner import TestCase, run_tests

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "4\n3 1 4 2\n10 20 30 40", "60"),
    TestCase("Sample 2", "1\n1\n10", "10"),
    TestCase("Sample 3", "5\n1 2 3 4 5\n1000000000 1000000000 1000000000 1000000000 1000000000", "5000000000"),
    TestCase("Sample 4", "9\n4 2 5 8 3 6 1 7 9\n6 8 8 4 6 3 5 7 5", "31"),
    
    # Edge Cases
    TestCase("Decreasing height", "3\n3 2 1\n10 20 30", "30"),
    TestCase("Increasing height", "3\n1 2 3\n10 20 30", "60"),
]

if __name__ == "__main__":
    run_tests("q", TEST_CASES)
