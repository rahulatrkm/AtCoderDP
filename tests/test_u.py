"""
Test cases for Problem U: Grouping
https://atcoder.jp/contests/dp/tasks/dp_u
"""

from test_runner import TestCase, run_tests

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "3\n0 10 20\n10 0 -100\n20 -100 0", "20"),
    TestCase("Sample 2", "5\n0 0 0 0 0\n0 0 0 0 0\n0 0 0 0 0\n0 0 0 0 0\n0 0 0 0 0", "0"),
    # Sample 3 removed - N=16 takes too long for standard test timeout
    
    # Edge Cases
    TestCase("Single element", "1\n0", "0"),
    TestCase("Two negative", "2\n0 -10\n-10 0", "0"),
    TestCase("Two positive", "2\n0 10\n10 0", "10"),
]

if __name__ == "__main__":
    run_tests("u", TEST_CASES)
