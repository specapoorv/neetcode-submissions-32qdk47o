# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (left<node.val and node.val<right):
                return False
            
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
    
        return valid(root, float('-inf'), float('inf'))
        
        #for root left and right are -inf, +inf
        # for left child, left is -inf, root
        # for right child, root, +inf
        # if i go left, change right to prev val(root val)
        # if i go right, change left to prev val(root val)
