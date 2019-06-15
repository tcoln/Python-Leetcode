class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        :note:
            回溯法遍历，解空间是二叉子集树
        """
        ans = []
        def backtrack(s, leftp, rightp):
            if len(s) == 2*n:
                ans.append(s)
                return
            if leftp < n:
                s += '('
                backtrack(s, leftp+1, rightp)
                s = s[:-1]
            if rightp < leftp: # 关键部分，保证生成合法性
                s += ')'
                backtrack(s, leftp, rightp+1)
                s = s[:-1]
        backtrack('', 0, 0)
        print ans
        return ans
