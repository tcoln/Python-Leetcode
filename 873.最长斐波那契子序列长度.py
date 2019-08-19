class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        :note:
            二维DP
            dp[i][j]表示以A[i]、A[j]作为最后两个数的序列最大长度，初始化时如果i==j,则dp[i][j]=0否则为2。
            从前往后遍历，i与i后面的j组成dp[i][j]，更新dp[j][k]，其中k= A[i] + A[j]
            例如，1+3=4，如果存在4，则dp[3][4] = dp[1][3] + 1
        """
        #A = [1,3,7,11,12,14,18]
        if not A:
            return 0
        l = len(A)
        dp = [[2 if i != j else 0  for j in range(l)] for i in range(l)]
        indexs = {}
        for i in range(l): indexs[A[i]] = i
        ans = 0
        for i in range(l):
            for j in range(i+1, l):
                s = A[i] + A[j]
                k = indexs.get(s, -1)
                if k != -1:
                    if dp[i][j] + 1 > dp[j][k]:
                        dp[j][k] = dp[i][j] + 1
                        ans = max(ans, dp[j][k])
        #print dp
        return ans if ans > 2 else 0 
