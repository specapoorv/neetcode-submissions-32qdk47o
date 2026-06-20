class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u,v,weight in flights:
            adj_list[u].append((v,weight))
        
        distance = [float('inf')]*n
        parent = [-1]*n
        distance[src] = 0
        for _ in range(k+1):
            updated = False
            temp = distance[:]
            for u in range(n):
                if distance[u] == float('inf'):
                    continue
                
                for v, weight in adj_list[u]:
                    if temp[v] > weight + distance[u]:
                        temp[v] = weight + distance[u]
                        parent[v] = u
                        updated = True
                    
            distance = temp
            if not updated:
                break
        
        return distance[dst] if distance[dst] != float('inf') else -1
