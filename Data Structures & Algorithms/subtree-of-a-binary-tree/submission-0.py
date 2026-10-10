# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if subRoot is null, it is automatically a subtree of root
        if not subRoot: return True
        if not root: return False
        
        if self.sameTree(root, subRoot):
            return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right
    
    def sameTree(self, p, q):
        # base cases
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        left = self.sameTree(p.left, q.left)
        right = self.sameTree(p.right, q.right)
        return left and right