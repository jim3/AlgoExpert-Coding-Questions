https://www.algoexpert.io/questions/find-closest-value-in-bst

```python
def findClosestValueInBst(tree, target):
    if tree is None:
        return False
    if tree.value == target:
        return True
    elif tree.value < target:
        return findClosestValueInBst(tree.right, target)
    else:
        return findClosestValueInBst(tree.left, target)

```

Write a function that takes in a Binary Search Tree (`BST`) and a
target integer value and returns the closest value to that target
value contained in the `BST`.

You can assume that there will only be one closest value.

Each `BST` node has an integer `value`, a `left` child node, and a
`right` child node. A node is said to be a valid `BST` node if and
only if it satisfies the `BST` property: its `value` is strictly
greater than the values of every node to its left; its `value` is less
than or equal to the values of every node to its right; and its
children nodes are either valid `BST` nodes themselves or `None /
null`.

---

### Binary Search Trees

A "Binary Search Tree", or `BST`, is a rooted binary tree with the value of each internal `node` being greater than all the values in the respective node's `left subtree` and less than the ones in its `right subtree`.

This is _NOT_ a BST b/c `8 < 6` in the left node subtree. It must be `< 6`!

```python
tree =   6
       /  \
      4    8
    /   \
   3     8
```

Not a BST!

```js
tree =    8
       /     \
      3      10
    /   \
   1     6
        /
       2
```

Is a BST!

```js
tree =    8
       /     \
      3      10
    /   \
   1     6
        /
       4
```

```js
tree =    7
       /     \
      2      11
        \
         5
        / \
       3   6
```

```python

tree =   10
       /     \
      5      15
    /   \   /   \
   2     5 13   22
 /           \
1            14

target = 12

Sample Output
13

```

**tree**

A Binary Tree is represented by a list of `nodes` and a `root` node.
Every node has to have a unique string `id` that will be referenced
by other nodes' `left` and `right` pointers and by the `root`.

```python
{
  "nodes": [
    {"id": "10", "left": "5", "right": "15", "value": 10},
    {"id": "15", "left": "13", "right": "22", "value": 15},
    {"id": "22", "left": null, "right": null, "value": 22},
    {"id": "13", "left": null, "right": "14", "value": 13},
    {"id": "14", "left": null, "right": null, "value": 14},
    {"id": "5", "left": "2", "right": "5-2", "value": 5},
    {"id": "5-2", "left": null, "right": null, "value": 5},
    {"id": "2", "left": "1", "right": null, "value": 2},
    {"id": "1", "left": null, "right": null, "value": 1}
  ],
  "root": "10"
}
```

### target

`12`

---
