class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root):
    if not root:
        return True
    
    def check(p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return check(p.left, q.right) and check(p.right, q.left)
    
    return check(root.left, root.right)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root.right = TreeNode(2, TreeNode(4), TreeNode(3))
    print(f"Is symmetric: {is_symmetric(root)}")
