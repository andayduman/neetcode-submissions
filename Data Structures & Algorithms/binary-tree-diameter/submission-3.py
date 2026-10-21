class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def height(node):
            if not node:
                return 0
            
            # Get heights of left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # The path length through this node is left_height + right_height
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            # Return the height of the current node to its parent
            return max(left_height, right_height) + 1
            
        height(root)
        return self.max_diameter