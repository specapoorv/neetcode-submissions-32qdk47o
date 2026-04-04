# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        height = 0
        def dfs(node):
            nonlocal height
            if not node: 
                return
            dfs(node.left)
            h_l = self.height(node.left)
            h_r = self.height(node.right)
            curr = h_l + h_r
            if curr > height:
                height = curr
            dfs(node.right)
        dfs(root)
        return height

    def height(self, node):
        if not node:
            return 0
        
        left = self.height(node.left)
        right = self.height(node.right)

        return 1 + max(left, right)


        
