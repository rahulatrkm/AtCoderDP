"""
Test cases for Problem Y: Grid 2
https://atcoder.jp/contests/dp/tasks/dp_y
"""

from test_runner import TestCase, run_tests

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "3 4 2\n2 2\n1 4", "3"),
    TestCase("Sample 2", "5 2 2\n2 1\n4 2", "0"),
    TestCase("Sample 3", "5 5 4\n3 1\n3 5\n1 3\n5 3", "24"),
    TestCase("Sample 4", "100000 100000 1\n50000 50000", "123445622"),
    
    # Edge Cases
    TestCase("No walls", "3 3 0", "6"),
    TestCase("Blocked start", "2 2 1\n1 1", "0"),
    TestCase("Blocked end", "2 2 1\n2 2", "0"),
]

if __name__ == "__main__":
    run_tests("y", TEST_CASES)
