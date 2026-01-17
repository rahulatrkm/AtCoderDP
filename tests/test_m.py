"""
Test cases for Problem M: Candies
https://atcoder.jp/contests/dp/tasks/dp_m
"""

from test_runner import TestCase, run_tests

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "3 4\n1 2 3", "5"),
    TestCase("Sample 2", "1 10\n9", "0"),
    TestCase("Sample 3", "2 0\n0 0", "1"),
    TestCase("Sample 4", "4 100000\n100000 100000 100000 100000", "665683269"),
    
    # Edge Cases
    TestCase("K=0", "3 0\n1 2 3", "1"),
    TestCase("Single child", "1 5\n10", "1"),
    TestCase("Exact match", "2 5\n3 2", "1"),
]

if __name__ == "__main__":
    run_tests("m", TEST_CASES)
