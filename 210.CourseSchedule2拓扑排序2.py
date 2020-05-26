import numpy as np

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        :note:
            之前是O(N^3)的时间复杂度，现在是O(N^2)
            用邻接表存储图，然后拓扑排序：循环找入度为0的点删除，并更新邻接表。
            核心数据结构：邻接表和节点入度统计数组
        """
        #numCourses, prerequisites = 2, [[0,1]] # [[0,1],[1,0]]
        #numCourses, prerequisites = 4, [[1,0],[2,0],[3,1],[3,2]]
        
        # 用邻接表表示有向图
        graph = {i:[] for i in range(numCourses)}
        indegree = np.zeros(numCourses)
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
            indegree[pair[0]] += 1
        #print graph, indegree
        
        # 拓扑排序
        visited = set()
        avisited = []
        while(True):
            hasCircle = True
            for key in graph.keys():
                if key not in visited and indegree[key] == 0:
                    hasCircle = False                    
                    for v in graph[key]:
                        indegree[v] -= 1
                    del graph[key]
                    visited.add(key)
                    avisited.append(key)
                    if len(avisited) == numCourses:
                        return avisited
            if hasCircle:
                return []
