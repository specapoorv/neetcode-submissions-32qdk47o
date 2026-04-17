class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(state, path, total):
            if total == target:
                result.append(path.copy())
                return
            if state >= len(nums) or total > target:
                return
            path.append(nums[state])
            dfs(state, path, total + nums[state])
            path.pop()
            dfs(state + 1, path, total)
        dfs(0, [], 0)
        return result
        
            
            
