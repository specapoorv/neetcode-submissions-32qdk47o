class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Since nodes are 1-indexed from 1 to n
        parent = {i: i for i in range(1, len(edges) + 1)}

        # Find function: finds the 'ultimate boss' (root) of a node
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i]) # Path compression shortcut
            return parent[i]

        # Union function: connects two nodes
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i == root_j:
                return False # They are already connected! A cycle is born.
            parent[root_i] = root_j
            return True

        # Process edges one by one in order
        for u, v in edges:
            if not union(u, v):
                return [u, v] # This edge completes the cycle and is the latest one!