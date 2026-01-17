"""
Understanding Lazy Propagation in Segment Trees

THE PROBLEM WITHOUT LAZY PROPAGATION:
--------------------------------------
Say we want to add +10 to range [2, 5] in an array of size 8.

Without lazy propagation, we'd have to:
1. Traverse down to every leaf in range [2, 5]
2. Update each leaf individually
3. Propagate changes back up to all ancestors

This touches O(n) nodes per range update! Too slow.

THE SOLUTION: LAZY PROPAGATION
-------------------------------
Key idea: Don't update immediately. Mark it as "lazy" and delay until needed.

Instead of updating all descendants immediately:
1. Store the update in lazy[node] at a high-level node
2. When we later visit that node, apply the lazy update then
3. Push the lazy value down to children (also lazily)

This makes range updates O(log n) instead of O(n)!

WHY WE PUSH BEFORE EVERY OPERATION:
------------------------------------
Before we read or modify a node, we MUST apply any pending updates first.

Example scenario:
1. Update range [0, 5] by +10 → lazy[root] = 10 (not applied yet)
2. Query range [2, 3] → We traverse through root
3. MUST call push(root) first! Otherwise we'd read stale value
4. push(root) applies the +10 and propagates to children

Without push(), we'd read incorrect values!

DETAILED EXAMPLE:
-----------------
Array size n=8, segment tree structure:

                      Node 1: [0,7]
                     /              \
            Node 2: [0,3]          Node 3: [4,7]
           /          \            /          \
      N4:[0,1]    N5:[2,3]    N6:[4,5]    N7:[6,7]
      /    \      /    \      /    \      /    \
    N8:0  N9:1 N10:2 N11:3 N12:4 N13:5 N14:6 N15:7

Initial state:
tree[all] = 0
lazy[all] = 0

OPERATION 1: Add +10 to range [0, 5]
-------------------------------------
update(1, 0, 7, 0, 5, +10)
  - Node 1 covers [0,7], want [0,5], need to split
  - push(1, 0, 7): lazy[1]=0, nothing to do
  
  update(2, 0, 3, 0, 3, +10)  # Left child, entire range
    - push(2, 0, 3): lazy[2]=0, nothing to do
    - [0,3] matches [0,3] exactly! 
    - lazy[2] = 10  ← MARK AS LAZY (don't go deeper!)
    - push(2, 0, 3): Apply immediately
      * tree[2] = 0 + 10 = 10
      * lazy[4] += 10 → lazy[4] = 10
      * lazy[5] += 10 → lazy[5] = 10
      * lazy[2] = 0 (cleared)
  
  update(3, 4, 7, 4, 5, +10)  # Right child, partial range
    - push(3, 4, 7): lazy[3]=0, nothing to do
    - [4,5] doesn't match [4,7], need to split
    
    update(6, 4, 5, 4, 5, +10)  # Left child of node 3
      - push(6, 4, 5): lazy[6]=0, nothing to do
      - [4,5] matches [4,5] exactly!
      - lazy[6] = 10  ← MARK AS LAZY
      - push(6, 4, 5): Apply immediately
        * tree[6] = 0 + 10 = 10
        * lazy[12] += 10 → lazy[12] = 10
        * lazy[13] += 10 → lazy[13] = 10
        * lazy[6] = 0 (cleared)

After operation 1:
tree[2] = 10, tree[6] = 10
lazy[4] = 10, lazy[5] = 10, lazy[12] = 10, lazy[13] = 10
(Other nodes haven't been touched - this is the key!)

OPERATION 2: Query max in range [2, 3]
---------------------------------------
query(1, 0, 7, 2, 3)
  - push(1, 0, 7): lazy[1]=0, nothing to do
  - [2,3] doesn't match [0,7], need to split
  
  query(2, 0, 3, 2, 3)  # Left child
    - push(2, 0, 3): lazy[2]=0, nothing to do ← (already pushed!)
    - [2,3] doesn't match [0,3], need to split
    
    query(5, 2, 3, 2, 3)  # Node 5
      - push(5, 2, 3): lazy[5]=10! ← HERE'S WHY WE PUSH!
        * tree[5] = 0 + 10 = 10
        * lazy[10] += 10 → lazy[10] = 10
        * lazy[11] += 10 → lazy[11] = 10
        * lazy[5] = 0
      - [2,3] matches [2,3] exactly!
      - return tree[5] = 10 ✓

If we DIDN'T call push(5), we'd return tree[5]=0 which is WRONG!
The correct value is 10 because of the pending update from operation 1.

KEY INSIGHT:
------------
lazy[node] stores "pending updates" that haven't been applied to descendants yet.

push() is called to ensure:
1. Current node has the correct value (apply lazy[node] to tree[node])
2. Children inherit the pending update (propagate to lazy[children])
3. Current lazy value is cleared (lazy[node] = 0)

We push() at the START of every operation because:
- update(): Need correct current value before modifying
- query(): Need correct current value before returning
- Without push(), we'd work with stale/incorrect data

ANALOGY:
--------
Think of lazy propagation like email notifications:

Without lazy:
- Send individual email to EVERY employee immediately (slow!)

With lazy:
- Send to department head, mark as "pending"
- When department head is contacted, they forward to their team
- Only the people actually involved get the message (efficient!)

push() = "Forward pending messages before doing anything else"
"""

def demonstrate_lazy_vs_normal():
    print("=" * 70)
    print("LAZY PROPAGATION DEMONSTRATION")
    print("=" * 70)
    
    print("\nScenario: Array of size 8, update range [0, 5] by +10")
    print()
    
    print("WITHOUT LAZY PROPAGATION:")
    print("  Must visit every leaf in [0, 5]:")
    print("  - Node 8 (position 0): tree[8] += 10")
    print("  - Node 9 (position 1): tree[9] += 10")
    print("  - Node 10 (position 2): tree[10] += 10")
    print("  - Node 11 (position 3): tree[11] += 10")
    print("  - Node 12 (position 4): tree[12] += 10")
    print("  - Node 13 (position 5): tree[13] += 10")
    print("  Plus update all ancestors: nodes 4,5,6,2,3,1")
    print("  Total: ~12 nodes touched")
    print()
    
    print("WITH LAZY PROPAGATION:")
    print("  Only mark high-level nodes:")
    print("  - Node 2 [0,3]: lazy[2] = 10")
    print("  - Node 6 [4,5]: lazy[6] = 10")
    print("  Total: ~8 nodes touched")
    print("  Updates to leaves delayed until needed!")
    print()
    
    print("=" * 70)
    print("WHY PUSH() IS NECESSARY")
    print("=" * 70)
    print()
    print("After marking lazy[2] = 10 (covers positions 0-3):")
    print()
    print("If we query position 2 WITHOUT push():")
    print("  - Traverse: Node 1 → Node 2 → Node 5 → Node 10")
    print("  - Read tree[10] = 0  ← WRONG! Missed the +10 update")
    print()
    print("If we query position 2 WITH push():")
    print("  - Traverse: Node 1 → Node 2")
    print("  - push(2): Propagate lazy[2]=10 to children")
    print("    * lazy[4] = 10, lazy[5] = 10")
    print("  - Continue: Node 5")
    print("  - push(5): Apply lazy[5]=10")
    print("    * tree[5] = 0 + 10 = 10")
    print("  - Read tree[5] = 10  ← CORRECT!")
    print()
    
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print("Lazy propagation: Delay updates until needed")
    print("push(): Apply delayed updates before reading/modifying")
    print("Benefit: O(log n) per operation instead of O(n)")
    print()
    print("Without push(), you'd read stale data!")
    print("With push(), you always get up-to-date values!")

if __name__ == "__main__":
    demonstrate_lazy_vs_normal()
