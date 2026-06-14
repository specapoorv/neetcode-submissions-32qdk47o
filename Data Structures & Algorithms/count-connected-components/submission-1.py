class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency_list = defaultdict(list)
        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])
            adjacency_list[edge[1]].append(edge[0])

        print(adjacency_list)
        visited = [False]*n

        def dfs(u):
            visited[u] = True
            for v in adjacency_list[u]:
                if not visited[v]:
                    dfs(v)

        counter = 0
        while not all(visited):
            counter +=1
            for index, val in enumerate(visited):
                if not val:
                    dfs(index)
                    break

        return counter