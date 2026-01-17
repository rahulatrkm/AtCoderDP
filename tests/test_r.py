"""
Test cases for Problem R: Walk
https://atcoder.jp/contests/dp/tasks/dp_r
"""

from test_runner import TestCase, run_tests

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "4 2\n0 1 0 0\n0 0 1 1\n0 0 0 1\n1 0 0 0", "6"),
    TestCase("Sample 2", "3 3\n0 1 0\n1 0 1\n0 0 0", "3"),
    TestCase("Sample 3", "6 2\n0 0 0 0 0 0\n0 0 1 0 0 0\n0 0 0 0 0 0\n0 0 0 0 1 0\n0 0 0 0 0 1\n0 0 0 0 0 0", "1"),
    TestCase("Sample 4", "1 1\n0", "0"),
    
    # Edge Cases
    TestCase("Self loop", "1 2\n1", "1"),
    TestCase("No edges", "2 1\n0 0\n0 0", "0"),
]

if __name__ == "__main__":
    run_tests("r", TEST_CASES)
