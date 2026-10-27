# BST · Stack · Queue — Exam Cheatsheet

## 1. Binary Search Tree
**Rule:** for *every* node, all keys in the left subtree < node < all keys in the right subtree. Checking only the direct children is **not enough**. This is a common trap.
**Terms:** root, leaf (no children), internal node, depth (edges from the root), height (edges on the longest root→leaf path; empty = −1, single node = 0, but check your course's convention).
**Shape depends on insert order:** inserting 1,2,3,4,5 gives a chain, so height = n−1 and operations cost O(n). A random order gives about O(log n).

**Init:** an empty tree is a null root. The first inserted key becomes the root.
**Insert:** start at the root. If the key is smaller go left, if larger go right, and repeat until you reach an empty spot. **A new node is always a leaf.**
> Insert 50, 30, 70, 20, 40, 60, 80 → root 50; 30 and 70 under it; 20 and 40 under 30; 60 and 80 under 70.

**Search:** follow the same path as insert. The number of comparisons is at most height + 1.
**Min / Max:** the leftmost node / the rightmost node.
**Successor:** the min of the right subtree. **Predecessor:** the max of the left subtree.

**Delete — 3 cases:**
1. **Leaf:** just remove it.
2. **One child:** connect the child to the deleted node's parent.
3. **Two children:** replace the key with its **in-order successor** (or predecessor), then delete that node. It always falls under case 1 or 2.
> Delete 50 from the tree above: the successor is 60, so 60 becomes the root.

## 2. Traversals (each visits all n nodes → O(n))
| Name | Order | Remember | Tree above gives |
|---|---|---|---|
| Pre-order | Node, Left, Right | root comes **first** | 50 30 20 40 70 60 80 |
| In-order | Left, Node, Right | **sorted** order | 20 30 40 50 60 70 80 |
| Post-order | Left, Right, Node | root comes **last** | 20 40 30 60 80 70 50 |
| Level-order | top to bottom, left to right | uses a **queue** | 50 30 70 20 40 60 80 |

- **Rebuilding a tree:** you need in-order **plus** either pre-order or post-order. The first element of pre-order (or last of post-order) is the root. Split the in-order list around the root and recurse on each side.
- In a BST, **pre-order alone** is enough to rebuild the tree: insert the keys in that order.

## 3. Complexity
| | Best/Avg (balanced) | Worst (skewed) |
|---|---|---|
| BST search / insert / delete | O(log n) | O(n) |
| Traversal | O(n) | O(n) |
| Stack and queue operations | O(1) | O(1) |

## 4. Stack — LIFO (last in, first out)
**Operations:** push, pop, peek/top, isEmpty. Pop on an empty stack causes **underflow**; push onto a full array causes **overflow**.
**Implementation:** an array with a top index, or a linked list where you push and pop at the head.
**Trace example:** push 1, push 2, pop, push 3, push 4, pop, pop → the pops return **2, 4, 3**, and the stack ends as [1].
**Uses:** recursion and the call stack, undo, bracket matching, postfix evaluation, reversing a sequence.
- **Postfix evaluation:** push numbers. On an operator, pop b, then pop a, and push a op b. For example, `5 3 2 * +` = 11.

## 5. Queue — FIFO (first in, first out)
**Operations:** enqueue (at the rear), dequeue (from the front), peek/front, isEmpty.
**Trace example:** enqueue 1, 2, 3, then dequeue, then enqueue 4, then dequeue → the dequeues return **1, 2**, and the queue ends as [3, 4].
**Circular array:** indices move forward with `i = (i + 1) % capacity`, which avoids wasting freed space at the front.
- Empty: `front == rear`, or count = 0
- Full: `(rear + 1) % capacity == front` (this version leaves one slot unused)

**Variants:** a deque allows both ends; a priority queue removes by priority (usually built on a heap).
**Uses:** level-order traversal, CPU/print scheduling, waiting lines, buffers.

## 6. Quick contrasts and exam traps
- **Stack goes with recursion and reversing; queue goes with level-order and taking turns.**
- A stack has only one open end (top); a queue has two (front and rear).
- A BST in-order traversal that isn't sorted means the tree isn't a valid BST.
- Duplicate keys: state your rule (ignore them, or always send them left or right).
- For delete with two children, use either the successor or the predecessor, but stay consistent, since they produce different trees.
- Draw the tree after **every** insert or delete; don't try to do it in your head.
