"""
Test cases for Problem N: Slimes
https://atcoder.jp/contests/dp/tasks/dp_n
"""

from test_runner import TestCase, run_tests

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "4\n10 20 30 40", "190"),
    TestCase("Sample 2", "5\n10 10 10 10 10", "120"),
    TestCase("Sample 3", "3\n1000000000 1000000000 1000000000", "5000000000"),
    TestCase("Sample 4", "6\n7 6 8 6 1 1", "68"),
    
    # Edge Cases
    TestCase("Two slimes", "2\n5 10", "15"),
    TestCase("All same", "3\n10 10 10", "50"),
]

if __name__ == "__main__":
    run_tests("n", TEST_CASES)
