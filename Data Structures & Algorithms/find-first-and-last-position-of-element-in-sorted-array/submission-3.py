class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r  = 0 , len(nums) - 1
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]

        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                r = mid -1
            elif nums[mid] <= target:
                l = mid + 1

        if nums[mid] != target:
            return [-1, -1]

        p1, p2 = mid, mid
        p1_found, p2_found = False, False   
        while p1>=0 and nums[p1]==target:
            p1=p1-1
        while p2<len(nums) and nums[p2]==target:
            p2=p2+1
        return[p1+1,p2-1]