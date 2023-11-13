# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root,root)
    def isMirror(self, root1: Optional[TreeNode],root2: Optional[TreeNode])->bool:
        if not(root1) and not(root2):
            return True
        if not(root1) or not(root2):
            return False
        return root1.val==root2.val and (self.isMirror(root1.left,root2.right)) and (self.isMirror(root1.right, root2.left))        