class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates = sorted(candidates)
        def backtrack(state, path, sum_of_path):
            if sum_of_path == target:
                result.append(path[:])
                return
            if sum_of_path > target:
                return
            
            for i in range(state, len(candidates)):
                if i > state and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                sum_of_path += candidates[i]
                backtrack(i+1, path, sum_of_path)
                to_remove = path[-1]
                path.pop()
                sum_of_path -= to_remove

            
        backtrack(0, [], 0)
        return result