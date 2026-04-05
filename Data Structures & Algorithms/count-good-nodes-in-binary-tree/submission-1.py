# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def traverse(node, largest):
            nonlocal res
            if not node:
                return
            
            if node.val >= largest:
                res +=1 
                largest = node.val
            
            traverse(node.left, largest)
            traverse(node.right, largest)
        
        traverse(root, float('-inf'))
        return res


        