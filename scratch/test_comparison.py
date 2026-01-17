'''
Compare the updated code with bottom-up
'''

from v import helper, helper_bottom_up

test_cases = [
    (2, [(1, 2)], 100, "2 nodes"),
    (3, [(1, 2), (1, 3)], 100, "3 nodes star"),
    (5, [(1, 2), (2, 3), (3, 4), (4, 5)], 1000, "5 nodes linear"),
    (5, [(1, 2), (1, 3), (1, 4), (1, 5)], 1000, "5 nodes star"),
]

print("=" * 70)
print("COMPARING YOUR CODE (UPDATED) WITH BOTTOM-UP")
print("=" * 70)

all_match = True

for n, edges, m, desc in test_cases:
    result_yours = helper(n, edges, m)
    result_bu = helper_bottom_up(n, edges, m)
    
    match = result_yours == result_bu
    status = "✓ MATCH" if match else "✗ DIFFER"
    
    print(f"\n{desc} (n={n}):")
    print(f"  Your code:  {result_yours}")
    print(f"  Bottom-up:  {result_bu}")
    print(f"  {status}")
    
    if not match:
        all_match = False

print("\n" + "=" * 70)
if all_match:
    print("✓ SUCCESS! Your code now matches bottom-up (mathematically correct)")
    print("The 'par' parameter helped, but they still differ because:")
    print("  • Your code still uses vis set differently")
    print("  • Cache behavior creates different results")
else:
    print("✗ Your code still differs from bottom-up")
    print("\nThe 'par' parameter doesn't fully fix the issue because:")
    print("  • vis is still a closure variable")
    print("  • Cache stores (node, col, par) but vis state still varies")
print("=" * 70)
