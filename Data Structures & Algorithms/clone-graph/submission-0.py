"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # Maps original node -> cloned node
        hashMap = {}
        
        def dfs(curr):
            # If we've already cloned this node, return its clone from the hash map
            if curr in hashMap:
                return hashMap[curr]
            
            # Create the clone for the current node and store it immediately
            # (Doing this before visiting neighbors prevents infinite loops in cycles)
            copy = Node(curr.val)
            hashMap[curr] = copy
            
            # Recursively clone all neighbors and add them to the copy's neighbors list
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy
        
        return dfs(node)