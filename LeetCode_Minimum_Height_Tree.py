#need to put in more time to understand this 

from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n==1:
            return [0]

        D = defaultdict(list)
        for u,v in edges:
            D[u].append(v)
            D[v].append(u)

        edge_cnt = {}
        leaves = deque()
        for src, neighbors in D.items():
            if len(neighbors) == 1:
                leaves.append(src)
            edge_cnt[src]=len(neighbors)

        while leaves:
            if n<=2:
                return list(leaves)
            for i in range(len(leaves)):
                node = leaves.popleft()
                n-=1
                for nei in D[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)