"""
Test cases for Problem X: Tower
https://atcoder.jp/contests/dp/tasks/dp_x
"""

from test_runner import TestCase, run_tests

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "3\n2 2 20\n2 1 30\n3 1 40", "50"),
    TestCase("Sample 2", "4\n1 2 10\n3 1 10\n2 4 10\n1 6 10", "40"),
    TestCase("Sample 3", "5\n1 10000 1000000000\n1 10000 1000000000\n1 10000 1000000000\n1 10000 1000000000\n1 10000 1000000000", "5000000000"),
    TestCase("Sample 4", "8\n9 5 7\n6 2 7\n5 7 3\n7 8 8\n1 9 6\n3 3 3\n4 1 7\n4 5 5", "22"),
    
    # Edge Cases
    TestCase("Single block", "1\n10 5 100", "100"),
    TestCase("Can't stack", "2\n10 1 50\n10 1 50", "50"),
]

if __name__ == "__main__":
    run_tests("x", TEST_CASES)
