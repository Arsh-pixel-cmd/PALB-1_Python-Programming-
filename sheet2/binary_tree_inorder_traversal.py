class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    res = []
    def helper(node):
        if node:
            helper(node.left)
            res.append(node.val)
            helper(node.right)
    helper(root)
    return res

if __name__ == "__main__":
    # Example tree
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(f"Inorder Traversal: {inorder_traversal(root)}")
