# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        seen = {}   # original node -> cloned node

        def dfs(node):
            if node in seen:
                return seen[node]

            # Create the clone first
            cp_node = Node(node.val)
            seen[node] = cp_node

            # Then clone its neighbors
            for n in node.neighbors:
                cp_node.neighbors.append(dfs(n))

            return cp_node

        return dfs(node)