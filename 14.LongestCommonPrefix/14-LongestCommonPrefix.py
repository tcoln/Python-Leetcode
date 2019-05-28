class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        :note:
            找到最小的字符串长度，然后依次比较每个字符串的第i个字符
        """
        #strs = []
        nStrs = len(strs)
        minL = float('Inf')
        ans = ''
        if nStrs == 0:
            return ans
        for i in range(nStrs):
            a = len(strs[i]) 
            if a < minL:
                minL = a
        for i in range(minL):
            for j in range(1, nStrs):
                if strs[0][i] != strs[j][i]:
                    return ans
            ans += strs[0][i]
        return ans
