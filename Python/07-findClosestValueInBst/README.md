### [Find Closest Value in a Binary Search Tree](https://www.algoexpert.io/questions/find-closest-value-in-bst)

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

**tree**

A `Binary Tree` is represented by a list of `nodes` and a `root` node.
Every node has to have a unique string `id` that will be referenced
by other nodes' `left` and `right` pointers and by the `root`.

```json
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

