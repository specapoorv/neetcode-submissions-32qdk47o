import heapq
from typing import List
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. Build the adjacency list for O(1) neighbor lookups
        graph = defaultdict(list)
        for ui, vi, ti in times:
            graph[ui].append((vi, ti))
            
        pq = [(0, k)]
        distances = [float("inf")] * n
        distances[k-1] = 0  # FIX 1: Set the source node distance to 0

        while pq:
            current_dist, u = heapq.heappop(pq)
            
            if current_dist > distances[u-1]:
                continue
            
            # FIX 2: Only iterate over the actual neighbors of 'u'
            for vi, ti in graph[u]:
                new_dist = current_dist + ti
                if new_dist < distances[vi-1]:
                    distances[vi-1] = new_dist
                    heapq.heappush(pq, (new_dist, vi))
        
        # Since we initialized the array with exactly size n, 
        # we check all nodes (no slicing needed)
        ans = max(distances) 
        
        return ans if ans != float('inf') else -1