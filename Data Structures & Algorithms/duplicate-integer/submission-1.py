class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num]+= 1
            else:
                seen[num]= 1
        
        return any(count > 1 for count in seen.values())