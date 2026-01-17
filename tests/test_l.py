"""
Test cases for Problem L: Deque
https://atcoder.jp/contests/dp/tasks/dp_l
"""

from test_runner import TestCase, run_tests

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "4\n10 80 90 30", "10"),
    TestCase("Sample 2", "3\n10 100 10", "-80"),
    TestCase("Sample 3", "1\n10", "10"),
    TestCase("Sample 4", "10\n1000000000 1 1000000000 1 1000000000 1 1000000000 1 1000000000 1", "4999999995"),
    TestCase("Sample 5", "6\n4 2 9 7 1 5", "2"),
    
    # Edge Cases
    TestCase("Two elements", "2\n5 10", "5"),
    TestCase("All same", "4\n10 10 10 10", "0"),
]

if __name__ == "__main__":
    run_tests("l", TEST_CASES)
