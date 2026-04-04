# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        max = 0
        def traverse(node):
            nonlocal count
            nonlocal max

            if not node: 
                return None
            count += 1

            if count > max:
                max = count
            traverse(node.left)
            traverse(node.right)
            count -= 1

        traverse(root)
        return max
