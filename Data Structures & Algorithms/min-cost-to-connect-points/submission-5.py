class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        parent = [i for i in range(n)]
        rank = [0]*n
        def union(i, j):
            root_i = find(i)
            root_j = find(j)

            if root_i == root_j:
                return False
            
            # Always compare ranks and attach ROOTS, not the original elements
            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            elif rank[root_i] > rank[root_j]:
                parent[root_j] = root_i
            else:
                parent[root_i] = root_j
                rank[root_j] += 1
            
            return True
            

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        edges = []
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                edges.append((dist, i, j))
        
        edges.sort()

        mst_weight = 0
        edges_used = 0 
    
        for weight, u, v in edges:
            if union(u,v):
                mst_weight += weight
                edges_used += 1

                if edges_used == n-1:
                    break
            
        return mst_weight

            


    
