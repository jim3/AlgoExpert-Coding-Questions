Write a function that takes in a **Binary Tree** and returns a list of its branch
sums ordered from _leftmost_ branch sum to _rightmost_ branch sum.

A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree
branch is a path of nodes in a tree that starts at the root node and ends at
any _leaf node_.

Each BinaryTree node has an integer value, a _left child node_, and a _right child node_.

Children nodes can either be BinaryTree nodes themselves or `None / null`.

> Sample Input

```
tree =     1
        /     \
       2       3
     /   \    /  \
    4     5  6    7
  /   \  /
 8    9 10

```

> Sample Output: `[15, 16, 18, 10, 11]`

```
15 == 1 + 2 + 4 + 8`
16 == 1 + 2 + 4 + 9
18 == 1 + 2 + 5 + 10
10 == 1 + 3 + 6
11 == 1 + 3 + 7
```

---

Notes

**In-order Traversal**

`In-order traversal` visits the left branch first, then the current node, and finally the right branch.

The diagram shows the traversal order of an in-order traversal on a binary tree.

**Pre-order Traversal**

`Pre-order traversal` visits the current node first, then the left subtree, and finally the right subtree.

**Post-order Traversal**

`Post-order traversal` visits the left subtree first, then the right subtree, and finally the current node.

### In-order Traversal

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def in_order_traversal(root: Node):
    if root is not None:
        in_order_traversal(root.left)
        print(root.val)
        in_order_traversal(root.right)

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    in_order_traversal(root)

```

---

> A Binary Tree is represented by a list of `nodes` and a `root` node. Every node has to have a unique string `id` that will be referenced by other nodes' `left` and `right` pointers and by the `root`.

```json
{
  "nodes": [
    { "id": "1", "left": "2", "right": "3", "value": 1 },
    { "id": "2", "left": "4", "right": "5", "value": 2 },
    { "id": "3", "left": "6", "right": "7", "value": 3 },
    { "id": "4", "left": "8", "right": "9", "value": 4 },
    { "id": "5", "left": "10", "right": null, "value": 5 },
    { "id": "6", "left": null, "right": null, "value": 6 },
    { "id": "7", "left": null, "right": null, "value": 7 },
    { "id": "8", "left": null, "right": null, "value": 8 },
    { "id": "9", "left": null, "right": null, "value": 9 },
    { "id": "10", "left": null, "right": null, "value": 10 }
  ],
  "root": "1"
}
```

---

```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Example Tree construction from the given data
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)
root.left.right.left = TreeNode(10)

def pre_order_traversal(node):
    if not node:
        return []
    print([node.value] + pre_order_traversal(node.left) + pre_order_traversal(node.right))
    return [node.value] + pre_order_traversal(node.left) + pre_order_traversal(node.right)

def in_order_traversal(node):
    if not node:
        return []
    return in_order_traversal(node.left) + [node.value] + in_order_traversal(node.right)

def post_order_traversal(node):
    if not node:
        return []
    return post_order_traversal(node.left) + post_order_traversal(node.right) + [node.value]

# Test the traversal functions
print("Pre-order traversal:", pre_order_traversal(root))
print("In-order traversal:", in_order_traversal(root))
print("Post-order traversal:", post_order_traversal(root))

```
