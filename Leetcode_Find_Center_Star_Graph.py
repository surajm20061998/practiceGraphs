#Intuition : For all the edges a->b increment the count of a and b, then check for final condition.
from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        D=defaultdict(int)

        for u,v in edges:
            D[u]+=1
            D[v]+=1

        n = len(D)
        for k,v in D.items():
            print(k, ":", v)
            if v==n-1:
                return k
        