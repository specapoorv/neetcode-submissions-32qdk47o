class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        rob1, rob2 = 0, 0
        res = 0
        for i, n in enumerate(nums):
            if i == 0:
                continue

            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        res = rob2
        print(res)
        rob1, rob2 = 0, 0
        for i, n in enumerate(nums):
            if i == len(nums) - 1:
                continue

            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        print(rob2)
        res = rob2 if rob2 > res else res
        return res



            



        