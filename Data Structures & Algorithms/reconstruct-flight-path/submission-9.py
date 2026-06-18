from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 1. Build the adjacency list
        adj_list = defaultdict(list)
        for ticket in tickets:
            adj_list[ticket[0]].append(ticket[1])
            
        # Total number of tickets we MUST use
        total_tickets = len(tickets)
        
        res = ["JFK"]
        # Using a list or dictionary to track used ticket indices 
        # handles duplicate flights between the same airports correctly
        visited = [False] * total_tickets 

        def dfs(node):
            # BASE CASE: If our itinerary length equals total tickets + 1,
            # we have successfully used every single ticket exactly once.
            if len(res) == total_tickets + 1:
                return True
                
            # Sort the neighbors inline to guarantee we try lexicographically smaller paths first
            # We use enumerate(adj_list[node]) to track the exact ticket index
            neighbors = sorted(enumerate(adj_list[node]), key=lambda x: x[1])
            
            for original_idx, neighbor in neighbors:
                # We need to find the actual index of this ticket in the original 'tickets' list
                # to mark it as visited uniquely.
                for i, ticket in enumerate(tickets):
                    if not visited[i] and ticket[0] == node and ticket[1] == neighbor:
                        
                        # STEP 1: Make the choice (Forward Step)
                        visited[i] = True
                        res.append(neighbor)
                        
                        # STEP 2: Recursive exploration
                        # Ask the future if this choice leads to a successful itinerary
                        if dfs(neighbor):
                            return True # If it worked, pass the success up the chain!
                            
                        # STEP 3: Rollback (The Backtrack Step)
                        # If we reach here, the choice led to a dead end. Undo it!
                        visited[i] = False
                        res.pop()
                        
                        # Break out of the inner loop to avoid marking the same physical ticket twice
                        break 
                        
            # If we tried all available flights from this airport and none worked out
            return False

        dfs("JFK")
        return res