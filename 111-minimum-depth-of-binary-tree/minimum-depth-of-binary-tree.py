# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        a=1+self.minDepth(root.left)
        b=1+self.minDepth(root.right)
        if a<=1 or b<=1:
            return max(a,b)    
        return min(a,b)