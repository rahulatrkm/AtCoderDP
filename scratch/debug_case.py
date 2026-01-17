"""
Debug the failing test case
"""

# Test case:
# 3 positions (0, 1, 2)
# Query 0: [0, 2] → +100 (if any '1' in positions 0,1,2)
# Query 1: [0, 0] → -10  (if '1' at position 0)
# Query 2: [1, 1] → -20  (if '1' at position 1)
# Query 3: [2, 2] → -30  (if '1' at position 2)

print("Possible configurations:")
print()

configs = [
    ("000", []),
    ("100", [0, 1]),  # pos 0: Query 0 and Query 1
    ("010", [0, 2]),  # pos 1: Query 0 and Query 2
    ("001", [0, 3]),  # pos 2: Query 0 and Query 3
    ("110", [0, 1, 2]),
    ("101", [0, 1, 3]),
    ("011", [0, 2, 3]),
    ("111", [0, 1, 2, 3]),
]

queries = [
    (0, 2, 100),
    (0, 0, -10),
    (1, 1, -20),
    (2, 2, -30),
]

for config, activated in configs:
    score = sum(queries[q][2] for q in activated)
    print(f"{config}: Queries {activated} → Score {score}")

print()
print("Expected answer: 70 (place '1' at position 2 only)")
