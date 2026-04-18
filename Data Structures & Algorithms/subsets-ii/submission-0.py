class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        
        def dfs(state, path):
            if state > len(nums):
                return
            res.append(path[:])
            for i in range(state, len(nums)):
                if i>state and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()
            
        dfs(0, [])
        return res