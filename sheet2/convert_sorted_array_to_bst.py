class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sorted_array_to_bst(nums):
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])
    return root

def preorder_traversal(node):
    if not node:
        return []
    return [node.val] + preorder_traversal(node.left) + preorder_traversal(node.right)

if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    root = sorted_array_to_bst(nums)
    print(f"Preorder Traversal of BST: {preorder_traversal(root)}")
