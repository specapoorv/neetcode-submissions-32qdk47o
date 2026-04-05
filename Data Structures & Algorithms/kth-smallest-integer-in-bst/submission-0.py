# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        val = None
        def dfs(node):
            nonlocal count
            nonlocal val
            if not node:
                return 
            dfs(node.left)
            count += 1
            print(count)
            if count == k:
                val = node.val
            dfs(node.right)
            
        dfs(root)
        return val
        