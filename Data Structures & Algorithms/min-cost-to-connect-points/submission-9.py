class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        mst_weights = 0 
        visited = set()

        min_heap = [(0, 0)]

        while len(visited) != n:
            cost, u = heapq.heappop(min_heap)

            if u in visited:
                continue
            
            visited.add(u)
            mst_weights += cost
            
            for v in range(n):
                if v not in visited:
                    x1, y1 = points[u]
                    x2, y2 = points[v]
                    dist = abs(x2-x1) + abs(y2-y1)

                    heapq.heappush(min_heap, (dist, v))

        return mst_weights
