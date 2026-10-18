# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:

    def bstCheck(self, curr, minVal, maxVal):
        if curr is None:
            return True
        if curr.val <= minVal or curr.val >= maxVal:
            return False
        isLeftValid = self.bstCheck(curr.left, minVal, curr.val)
        isRightValid = self.bstCheck(curr.right, curr.val, maxVal)
        return isLeftValid and isRightValid

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        # depth-first search approach
        isLeftValid = self.bstCheck(root.left, -math.inf, root.val)
        isRightValid = self.bstCheck(root.right, root.val, math.inf)
        return isLeftValid and isRightValid