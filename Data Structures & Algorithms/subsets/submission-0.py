class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(state, path):
            #state equivalent to index here, iterating in nums
            print("current path", path)
            result.append(path[:])
            for i in range(state, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])  
        return result  

