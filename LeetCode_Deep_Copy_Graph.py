#Dfs approach
#Intuition, make copy of not just the nodes but the structure of the graph as well

from typing import Optional
from collections import defaultdict,deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        copyDict = {}

        def dfs(curr):
            if curr in copyDict:
                return copyDict[curr]
            copy = Node(curr.val)
            copyDict[curr] = copy

            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node)

        
        
#BFS Approach

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        copyDict = {}

        copyDict[node] = Node(node.val)

        q = deque([node])

        while q:
            curr = q.popleft()
            for nei in curr.neighbors:
                if nei not in copyDict:
                    copyDict[nei]=Node(nei.val)
                    q.append(nei)
                copyDict[curr].neighbors.append(copyDict[nei])
        return copyDict[node]