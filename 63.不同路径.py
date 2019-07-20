class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        :note:
            动态规划方法求解，当前位置路径数等于上边+左边位置的路径数之和
        """
        # solution 1 dp
        if obstacleGrid == None:
            return
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        paths = [[1 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    paths[i][j] = 0
                    
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] == 0:
                    up = 0 if i - 1 < 0 else paths[i-1][j]
                    left = 0 if j - 1 < 0 else paths[i][j-1]
                    paths[i][j] = up + left
                
        return paths[m-1][n-1]
        
        # solution 2 recursive
        if m == 1 or n == 1:
            return 1
        else:
            return self.uniquePaths(m, n-1) + self.uniquePaths(m-1, n)
