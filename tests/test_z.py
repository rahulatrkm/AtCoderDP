"""
Test cases for Problem Z: Frog 3
https://atcoder.jp/contests/dp/tasks/dp_z
"""

from test_runner import TestCase, run_tests

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "5 6\n1 2 3 4 5", "20"),
    TestCase("Sample 2", "2 1000000000000\n500000 1000000", "1250000000000"),
    TestCase("Sample 3", "8 5\n1 3 4 5 10 11 12 13", "62"),
    
    # Edge Cases
    TestCase("Two stones", "2 10\n1 2", "11"),
    TestCase("Large gap", "3 1\n1 100 101", "9804"),
]

if __name__ == "__main__":
    run_tests("z", TEST_CASES)
