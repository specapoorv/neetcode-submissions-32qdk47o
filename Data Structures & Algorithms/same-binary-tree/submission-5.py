# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        def dfs(node):
            if not node:
                yield None
                return
            yield node.val
            yield from dfs(node.left)
            yield from dfs(node.right)

        gen_p, gen_q = dfs(p), dfs(q)
        for x, y in zip_longest(gen_p, gen_q):
            print(x)
            print(y)
            print('---')
            if x!=y:
                return False
            
        return True
        