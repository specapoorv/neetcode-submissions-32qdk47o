class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        #whenever l > r return or else append
        def backtrack(l, r, path):
            if l >r:
                return
            if l<0 or r<0:
                return
            if r==0:
                res.append(path)
            
            path += ("(")
            l -= 1
            backtrack(l, r, path)
            to_pop = path[-1]
            if to_pop == "(":
                l += 1
            else:
                r += 1
            path = path[:-1]
            path += (")")
            r -= 1
            backtrack(l, r, path)

        backtrack(n, n, "")
        return res


