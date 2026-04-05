class Solution:
    def buildTree(self, preorder, inorder):
        
        def build(pre, ino):
            if not pre or not ino:
                return None

            root = pre[0]

            for i in range(len(ino)):
                if ino[i] == root:
                    root_idx = i
                    break

            lst = ino[:root_idx]
            rst = ino[root_idx+1:]

            left = build(pre[1:1+len(lst)], lst)
            right = build(pre[1+len(lst):], rst)

            return TreeNode(root, left, right)

        return build(preorder, inorder)