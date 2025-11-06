from collections import defaultdict
from sortedcontainers import SortedSet

class Solution(object):
    def processQueries(self, c, connections, queries):
        """
        :type c: int
        :type connections: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # Step 1: build the graph
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: find connected components using DFS
        comp_id = [-1] * (c + 1)  # component id for each station
        cid = 0
        
        def dfs(u, curr):
            comp_id[u] = curr
            for v in graph[u]:
                if comp_id[v] == -1:
                    dfs(v, curr)
        
        for i in range(1, c+1):
            if comp_id[i] == -1:
                dfs(i, cid)
                cid += 1
        
        # Step 3: maintain online stations per component
        online = [SortedSet() for _ in range(cid)]
        for i in range(1, c+1):
            online[comp_id[i]].add(i)
        
        # Step 4: process queries
        result = []
        status = [True] * (c + 1)  # True = online, False = offline
        
        for qtype, x in queries:
            if qtype == 1:
                if status[x]:
                    result.append(x)
                else:
                    comp = comp_id[x]
                    if online[comp]:
                        result.append(online[comp][0])
                    else:
                        result.append(-1)
            else:  # qtype == 2
                if status[x]:
                    status[x] = False
                    online[comp_id[x]].remove(x)
        
        return result
