# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ok the optimal solution we dont need to call height func again and again we need to calculate
# diamter and return height
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(node):
            nonlocal diameter
            if not node:
                return 0 #we are returning height

            left, right = dfs(node.left), dfs(node.right)
            diameter = max(diameter, left + right)

            return 1 + max(left, right)
            
        dfs(root)
        return diameter


        
