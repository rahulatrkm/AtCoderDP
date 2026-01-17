"""
Test cases for Problem V: Subtree
https://atcoder.jp/contests/dp/tasks/dp_v
"""

from test_runner import TestCase, run_tests

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "3 100\n1 2\n2 3", "3\n4\n3", multiline=True),
    TestCase("Sample 2", "4 100\n1 2\n1 3\n1 4", "8\n5\n5\n5", multiline=True),
    TestCase("Sample 3", "1 100", "1", multiline=True),
    TestCase("Sample 4", "10 2\n8 5\n10 8\n6 5\n1 5\n4 8\n2 10\n3 6\n9 2\n1 7", "0\n0\n1\n1\n1\n0\n1\n0\n1\n1", multiline=True),
    
    # Edge Cases
    TestCase("Two nodes", "2 100\n1 2", "2\n2", multiline=True),
]

if __name__ == "__main__":
    run_tests("v", TEST_CASES)
