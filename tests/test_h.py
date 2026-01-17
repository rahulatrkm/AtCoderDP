"""
Test cases for Problem H: Grid 1
https://atcoder.jp/contests/dp/tasks/dp_h
"""

from test_runner import TestCase, run_tests

TEST_CASES = [
    # AtCoder Samples
    TestCase("Sample 1", "3 4\n...#\n.#..\n....", "3"),
    TestCase("Sample 2", "5 2\n..\n#.\n..\n.#\n..", "0"),
    TestCase("Sample 3", "5 5\n..#..\n.....\n#...#\n.....\n..#..", "24"),
    
    # Edge Cases
    TestCase("Min grid", "2 2\n..\n..", "2"),
    TestCase("Single path", "2 2\n.#\n..", "1"),
    TestCase("Blocked", "2 2\n.#\n#.", "0"),
    TestCase("1x1", "1 1\n.", "1"),
]

if __name__ == "__main__":
    run_tests("h", TEST_CASES)
