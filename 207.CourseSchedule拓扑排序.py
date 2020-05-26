import numpy as np

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        :note:
            用邻接矩阵存储图，然后拓扑排序：循环找入度为0的点删除，并更新邻接矩阵。
        """
        #numCourses, prerequisites = 2, [[0,1]] # [[0,1],[1,0]]
        #numCourses, prerequisites = 3, [[1,0],[1,2],[0,1]]
        
        # 用关联矩阵表示有向图
        graph = np.zeros((numCourses, numCourses))
        indegree = np.zeros(numCourses)
        for pair in prerequisites:
            graph[pair[1], pair[0]] = 1
            indegree[pair[0]] += 1
        #print graph, indegree
        
        # 拓扑排序
        count = 0
        visited = set()
        while(True):
            hasCircle = True
            for i in range(numCourses):
                if i not in visited and indegree[i] == 0:
                    hasCircle = False
                    for j in range(numCourses):
                        if graph[i,j] != 0:
                            graph[i,j] = 0
                            indegree[j] -= 1
                    visited.add(i)
                    count += 1
                    if count == numCourses:
                        return True
            if hasCircle:
                return False
