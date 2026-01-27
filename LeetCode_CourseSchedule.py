#convert list of dependencies to adjency list
#Do cycle detection in a graph
#If there is a cycle -> False
#               else -> True

from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        
        courses = prerequisites
        
        for a,b in courses:
            g[a].append(b)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED]*numCourses

        def dfs(node) : 
            state = states[node]
            if state == VISITED:
                return True
            elif state == VISITING:
                return False
            #If state is visiting that means we are back to the node we started on and that is a cycle

            states[node] = VISITING
            for nei in g[node]:
                if not dfs(nei) : return False
            
            states[node] = VISITED
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
            #if dfs gives false, that means there is a cycle ad hence not possible to complete all courses
        return True
        

#HOW TO DO THE SAME WITHOUT RECURSION?

from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        state = [UNVISITED] * numCourses

        for start in range(numCourses):
            if state[start] != UNVISITED:
                continue

            stack = [(start, 0)]  # (node, phase) phase=0 enter, phase=1 exit

            while stack:
                node, phase = stack.pop()

                if phase == 0:  # entering
                    if state[node] == VISITING:
                        return False  # back-edge -> cycle
                    if state[node] == VISITED:
                        continue

                    state[node] = VISITING
                    stack.append((node, 1))  # schedule exit

                    for nei in g[node]:
                        if state[nei] == VISITING:
                            return False
                        if state[nei] == UNVISITED:
                            stack.append((nei, 0))

                else:  # exiting
                    state[node] = VISITED

        return True