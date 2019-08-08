class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        :note:
            从回溯法到记忆递归（总分模式：假设子问题已经求解了，先求总解）再到动态规划（分总模式：先求子问题解再求总解）一步步提高效率，DP要考虑更多的边界条件。
        """
        if not s or len(s) == 1:
            return 0
        #3 动态规划 O(n^3)
        #s = "cbbbcc"
        #s = "cbb"
        l = len(s)
        dp = [0 for i in range(l)]
        for i in range(1, l):
            dp[i] = dp[i-1] + 1
            for j in range(i-1, -1, -1):
                rev = s[i:j-1:-1] if j-1 >=0 else s[i::-1]
                if s[j:i+1] == rev:                    
                    dp[i] = min(dp[i], dp[j-1]+1)
                    if j == 0:
                        dp[i] = 0
                #print s[j:i+1], rev,  dp[i]
            #print dp
        return dp[l-1]
        
        #2 记忆递归
        global words
        words = {}
        def recursion(s):
            global words
            words[s] = float('inf')
            if not s:
                return 0
            l = len(s)
            if l == 1:
                words[s] = 1
                return words[s]
            for i in range(l):
                if s[:i+1] == s[i::-1]:
                    if not words.has_key(s[i+1:]): words[s[i+1:]] = recursion(s[i+1:])
                    words[s] = min(words[s[i+1:]]+1, words[s])
            return words[s]      
        recursion(s)
        return words[s]-1
    
        #1 回溯法
        global minc
        minc = float('inf')
        def backtrack(s, path, cutn):
            global minc
            if not s:
                #print cutn
                if cutn < minc:
                    minc = cutn
            if cutn < minc-1:
                l = len(s)
                for i in range(l):
                    if s[:i+1] == s[i::-1]:
                        backtrack(s[i+1:], path+s[:i+1], cutn+1)        
        backtrack(s, '', 0)
        return minc - 1
