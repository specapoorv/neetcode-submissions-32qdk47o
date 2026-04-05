# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # the moment the split happens thats the common ancestor
        # so say 3 and 8 as p,q then roots going to be for sure inside 3,8 
        # for each node.val we will check if its greater or smaller if its greater go left
        # if its smaller go right, if in between thats the ancestor

        if p.val>q.val:
            p, q = q, p

        def traverse(node):
            if node.val > p.val and node.val > q.val:
                return traverse(node.left)
            if node.val < p.val and node.val < q.val:
                return traverse(node.right)
            if node.val >= p.val and node.val <= q.val:
                return node
        
        return traverse(root)
