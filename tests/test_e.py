"""
Test cases for Problem E: Knapsack 2
https://atcoder.jp/contests/dp/tasks/dp_e
"""

from test_runner import TestCase, run_tests

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "3 8\n3 30\n4 50\n5 60", "90"),
    TestCase("Sample 2", "1 1000000000\n1000000000 10", "10"),
    TestCase("Sample 3", "6 15\n6 5\n5 6\n6 4\n6 6\n3 5\n7 2", "17"),
    
    # Edge Cases
    TestCase("Large W small v", "3 1000000000\n1 1\n2 2\n3 3", "6"),
    TestCase("Single item", "1 100\n50 75", "75"),
    TestCase("All same value", "3 10\n3 10\n4 10\n5 10", "20"),
]

if __name__ == "__main__":
    run_tests("e", TEST_CASES)
