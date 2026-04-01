class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = float('inf')
        while l<=r:
            mid = l + (r-l) // 2
            current_h = self.get_hvalue(piles, mid)
            if current_h <= h:
                r = mid - 1
                k = mid
            elif current_h > h:
                l = mid + 1
        return k

    def get_hvalue(self, piles, k):
        h = sum((pile + k - 1) // k for pile in piles)
        return h 



        