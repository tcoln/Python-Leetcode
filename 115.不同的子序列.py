class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        :note:
            动态规划方法求解
            当最后一个字母不相等时候，必定删除S的最后一个字母，等于dp[i-1][j]，
            若相等，可以保留最后一个字母d[i-1][j-1]，还可以删除S最后一个字母d[i-1][j]
            注意初始化
            if S[i] == T[j]: dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:   dp[i][j] = dp[i-1][j]
        """
        rows = len(s)
        cols = len(t)
        ans = [[0 for j in range(cols + 1)] for i in range(rows + 1)]
        for i in range(rows):
            ans[i][0] = 1
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if s[i-1] == t[j-1]:
                    ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
                else:
                    ans[i][j] = ans[i-1][j]
        return ans[rows][cols]
        
