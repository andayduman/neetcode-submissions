# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] # resulting array that will hold the arrays of each level of the tree
        q = deque() # queue that will store nodes level by level

        q.append(root)
        while q:
            # atp we have all the nodes for the current level
            # so get it's length
            qLen = len(q) # this tells us how many times we will pop from the queue to get all the nodes in curent level
            lvlNodes = []
            for i in range(qLen):
                node = q.popleft()
                if node: # have to do this check because nodes at bottom of the tree have pointers to None
                    lvlNodes.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            # once we get to the bottom of the tree, null nodes will be added to lvlNodes even though it won't go into
            # the qLen loop, so just check that lvlNodes is non-empty before adding it to res
            if lvlNodes: 
                res.append(lvlNodes)
        return res