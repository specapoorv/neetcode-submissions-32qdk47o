class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(index, path):
            #our state is index, path is trajectory
            #base case, comparing with state because state holds the info for len(path)
            if index == len(digits):
                result.append(path)
                return

            # get letters for current digit = getting choices for the state
            letters = phone[digits[index]]

            for ch in letters: #for choice in choices
                # choose
                path += ch #update trajectory

                # explore = move state ahead
                backtrack(index + 1, path)

                # undo (important!)
                path = path[:-1]

        backtrack(0, "")
        return result