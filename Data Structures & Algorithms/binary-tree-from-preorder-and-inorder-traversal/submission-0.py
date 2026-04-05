# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root = preorder[0]
        idx = inorder.index(root)

        left = self.buildTree(preorder[1:1+idx], inorder[:idx])
        right = self.buildTree(preorder[1+idx:], inorder[idx+1:])

        return TreeNode(root, left, right)