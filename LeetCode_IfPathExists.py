from collections import defaultdict

class Solution:
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #convert list to adjency list

        D = defaultdict(list)

        for u,v in edges:
            D[u].append(v)
            D[v].append(u)
        
        seen = set()
        seen.add(source)
        stack = [source]

        while stack:
            node = stack.pop()
            print(node)
            if node == destination:
                return True
            for nei_node in D[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    stack.append(nei_node)
        
        return False
    
    
    
#HOW TO IMPLEMENT A RECURSIVE VERSION OF THE ABOVE SOLUTION


from collections import defaultdict

class Solution:
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #convert list to adjency list

        D = defaultdict(list)

        for u,v in edges:
            D[u].append(v)
            D[v].append(u)
        
        seen = set()
        seen.add(source)

        def dfs(node):
            print(node)
            if node == destination:
                return True
            seen.add(node)
            for nei in D[node]:
                if nei in seen:
                    continue
                if dfs(nei):
                    return True
            return False

        return dfs(source)
        