"""
Test cases for Problem P: Independent Set
https://atcoder.jp/contests/dp/tasks/dp_p
"""

from test_runner import TestCase, run_tests

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "3\n1 2\n2 3", "5"),
    TestCase("Sample 2", "4\n1 2\n1 3\n1 4", "9"),
    TestCase("Sample 3", "7\n1 2\n1 3\n2 4\n2 5\n3 6\n3 7", "41"),
    
    # Edge Cases
    TestCase("Single node", "1", "2"),
    TestCase("Two nodes", "2\n1 2", "3"),
    TestCase("Linear 4", "4\n1 2\n2 3\n3 4", "8"),
]

if __name__ == "__main__":
    run_tests("p", TEST_CASES)
