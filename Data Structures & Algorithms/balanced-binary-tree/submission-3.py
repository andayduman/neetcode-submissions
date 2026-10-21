# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
       # depth-first search
        if not root:
            return True

        self.result = True

        def check(node):
            if not node:
                return 0
            left = check(node.left)
            right = check(node.right)
            if abs(left - right) > 1:
                self.result = False
            return max(left, right) + 1

        check(root)
        return self.result