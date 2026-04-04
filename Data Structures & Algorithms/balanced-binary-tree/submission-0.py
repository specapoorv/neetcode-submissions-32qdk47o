# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def inorder_traversal(node):
            nonlocal res
            if not node:
                return
            h_l = self.calculate_height(node.left)
            print(h_l)
            h_r = self.calculate_height(node.right)
            print(h_r)
            height = abs(h_l-h_r)
            print(height)
            if height > 1:
                res = False
            inorder_traversal(node.left)
            inorder_traversal(node.right)
        
        inorder_traversal(root)
        return res

    def calculate_height(self, node):
        if not node:
            return 0
        left_h = self.calculate_height(node.left)
        right_h = self.calculate_height(node.right)
        return 1 + max(left_h, right_h)

        
        
        
            
            
            
        