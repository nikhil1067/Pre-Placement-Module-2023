# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        val=set()
        def inorder(node):
            if not node:
                return False
            if inorder(node.left):
                return True
            if node.val in val:
                return True
            val.add(k-node.val)
            if inorder(node.right):
                return True
            return False
        return inorder(root)