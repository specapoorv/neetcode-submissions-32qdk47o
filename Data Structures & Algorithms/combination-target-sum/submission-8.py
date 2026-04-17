class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(state, path, sum_of_path):
            if sum_of_path == target:
                result.append(path[:])
                return
            if sum_of_path > target:
                return
            
            for i in range(state, len(nums)):
                path.append(nums[i])
                sum_of_path += nums[i]
                backtrack(i, path, sum_of_path)
                to_remove = path[-1]
                path.pop()
                sum_of_path -= to_remove

            
        backtrack(0, [], 0)
        return result
