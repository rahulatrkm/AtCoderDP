"""
Test cases for Problem G: Longest Path
https://atcoder.jp/contests/dp/tasks/dp_g
"""

from test_runner import TestCase, run_tests

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "4 5\n1 2\n1 3\n3 2\n2 4\n3 4", "3"),
    TestCase("Sample 2", "6 3\n2 3\n4 5\n5 6", "2"),
    TestCase("Sample 3", "5 8\n5 3\n2 3\n2 4\n5 2\n5 1\n1 4\n4 3\n1 3", "3"),
    
    # Edge Cases
    TestCase("Single node", "1 0", "0"),
    TestCase("Two nodes", "2 1\n1 2", "1"),
    TestCase("Linear chain", "4 3\n1 2\n2 3\n3 4", "3"),
    TestCase("Star graph", "5 4\n1 2\n1 3\n1 4\n1 5", "1"),
]

if __name__ == "__main__":
    run_tests("g", TEST_CASES)
