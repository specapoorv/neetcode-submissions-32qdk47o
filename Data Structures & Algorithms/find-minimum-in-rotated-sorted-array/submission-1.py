class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float('inf')
        while l<=r:
            mid = l + (r-l) // 2
            if nums[l]<= nums[r]:
                #already sorted
                return nums[l]
            
            if nums[mid] < res:
                res = nums[mid]

            if nums[mid] >nums[r]:
                #check right
                l = mid+1

            elif nums[mid]<nums[r]:
                r = mid
        return nums

            

            
        