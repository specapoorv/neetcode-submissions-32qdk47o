class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]):
        adjacency_list = defaultdict(list)
        for preq in prerequisites:
            adjacency_list[preq[1]].append(preq[0])

        print(adjacency_list)

        visited = [False]*numCourses
        path = [False]*numCourses
        res = []

        def dfs(u):
            visited[u] = True
            path[u] = True

            for v in adjacency_list[u]:
                if path[v]:
                    return True
                
                if not visited[v]:
                    if dfs(v):
                        return True
            
            path[u] = False
            res.append(u)
            return False
        
        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return []

        return res[::-1]

        