class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)              

        count = sorted(count.items(), key=lambda item:item[1])
        res = count[:-k-1 :-1]
        return[val[0] for val in res]


        