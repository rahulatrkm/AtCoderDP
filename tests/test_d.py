"""
Test cases for Problem D: Knapsack 1
https://atcoder.jp/contests/dp/tasks/dp_d
"""

from test_runner import TestCase, run_tests

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "3 8\n3 30\n4 50\n5 60", "90"),
    TestCase("Sample 2", "5 5\n1 1000000000\n1 1000000000\n1 1000000000\n1 1000000000\n1 1000000000", "5000000000"),
    TestCase("Sample 3", "6 15\n6 5\n5 6\n6 4\n6 6\n3 5\n7 2", "17"),
    
    # Edge Cases
    TestCase("Single fits", "1 10\n5 100", "100"),
    TestCase("Single no fit", "1 10\n15 100", "0"),
    TestCase("All equal W", "3 10\n10 50\n10 100\n10 75", "100"),
    TestCase("All weight 1", "5 5\n1 10\n1 20\n1 30\n1 40\n1 50", "150"),
    TestCase("None fit", "3 5\n10 100\n20 200\n30 300", "0"),
    TestCase("Take all", "3 60\n10 100\n20 200\n30 300", "600"),
    TestCase("Greedy fails", "3 50\n10 60\n20 100\n30 120", "220"),
]

if __name__ == "__main__":
    run_tests("d", TEST_CASES)
