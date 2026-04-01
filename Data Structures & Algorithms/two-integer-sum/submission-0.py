class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in hash:
                return [hash[complement], index]
            hash[num] = index

        