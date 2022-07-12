# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        temp=[root]
        res=[]
        while temp:
            x1=[]
            x2=[]
            for i in temp:
                x2.append(i.val)
                if i.left:
                    x1.append(i.left)
                if i.right:
                    x1.append(i.right)
            res.append(x2)
            temp=x1    
        return res