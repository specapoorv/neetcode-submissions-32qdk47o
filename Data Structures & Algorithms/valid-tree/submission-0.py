class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacency_list = defaultdict(list)
        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])
            adjacency_list[edge[1]].append(edge[0])

        print(adjacency_list)
        visited = [False]*n

        def dfs(u, parent=-1):
            visited[u] = True
            for v in adjacency_list[u]:
                if not visited[v]:
                    if dfs(v, u):
                        return True
                
                elif v != parent:
                    return True
            
            return False
        
        cycle = dfs(0)
        if cycle:
            return False
        
        elif not all(visited):
            return False
        
        return True
            


        

        