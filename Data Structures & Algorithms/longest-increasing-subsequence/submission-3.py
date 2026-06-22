class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*(len(nums)+1)


        for i in range(1, len(nums)):
            print(nums[i])
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        print(dp) 
        return max(dp)
            
            