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

# `node` is the function parameter  | "node.right: " +
def pre_order_traversal(node):
    if not node:
        return []
    print([node.value] + pre_order_traversal(node.left) +  pre_order_traversal(node.right))
    return [node.value] + pre_order_traversal(node.left) + pre_order_traversal(node.right)

# Test the traversal functions
print("Pre-order traversal:", pre_order_traversal(root))
