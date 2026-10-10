# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        # recursive case:
        left_sub = self.isSameTree(p.left, q.left)
        right_sub = self.isSameTree(p.right, q.right)
        return left_sub and right_sub
        

        
