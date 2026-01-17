"""
Test cases for Problem W: Intervals
https://atcoder.jp/contests/dp/tasks/dp_w
"""

from test_runner import TestCase, run_tests

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "5 3\n1 3 10\n2 4 -10\n3 5 10", "20"),
    TestCase("Sample 2", "3 4\n1 3 100\n1 1 -10\n2 2 -20\n3 3 -30", "90"),
    TestCase("Sample 3", "1 1\n1 1 -10", "0"),
    TestCase("Sample 4", "1 5\n1 1 1000000000\n1 1 1000000000\n1 1 1000000000\n1 1 1000000000\n1 1 1000000000", "5000000000"),
    
    # Edge Cases
    TestCase("Single positive", "1 1\n1 1 10", "10"),
    TestCase("All negative", "2 2\n1 1 -5\n2 2 -5", "0"),
]

if __name__ == "__main__":
    run_tests("w", TEST_CASES)
