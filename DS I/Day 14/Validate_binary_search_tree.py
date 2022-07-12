# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isvalid(root, minval, maxval):
            if root is None:
                return True
            if root.val <= minval or root.val >= maxval:
                return False
            else:
                return isvalid(root.left, minval, root.val) and isvalid(root.right, root.val, maxval)
            
        return isvalid(root, -float("inf"), float("inf"))