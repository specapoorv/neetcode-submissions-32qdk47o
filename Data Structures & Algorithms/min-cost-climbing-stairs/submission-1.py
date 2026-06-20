class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # Base cases: standing at the top or past the top costs 0
        one = 0
        two = 0
        
        # Iterate backwards from the last step (n-1) down to 0
        for i in range(len(cost) - 1, -1, -1):
            # Total cost from step i = current step cost + min of taking 1 or 2 steps
            current = cost[i] + min(one, two)
            
            # Shift pointers backward
            two = one
            one = current
            
        # Since we can start at either index 0 or index 1, 
        # the answer is the minimum cost from those two entry points.
        return min(one, two)