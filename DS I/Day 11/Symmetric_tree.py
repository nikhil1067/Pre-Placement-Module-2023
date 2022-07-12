# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checksymmetry(x1, x2): 
            if not x1 and not x2:
                return True            
            if not x1 or not x2 or x1.val!=x2.val:
                return False 
            return checksymmetry(x1.left, x2.right) and checksymmetry(x1.right, x2.left)
        return checksymmetry(root.left, root.right)