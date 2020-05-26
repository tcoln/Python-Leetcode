class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
	:note: 统计以每个字符为结尾的最长不重复子串长度，每次统计的时候都要利用前一个字符的最长不重复子串长度来更新当前的；第二轮得到整个字符串的最长不重复子串长度
        """
        n = len(s)
        if n == 0:
            return 0
        maxLenStart = {}
        for i in range(n):
            if i == 0:
                maxLenStart[i] = i
            else:
                preStart = maxLenStart[i-1]
                maxLenStart[i] = preStart
                for j in range(i-1, preStart-1, -1):
                    if s[i] == s[j]:
                        maxLenStart[i] = j+1
        maxLen = 0
        for i in range(n):
            curMax = i - maxLenStart[i] + 1
            if maxLen < curMax:
                maxLen = curMax
        return maxLen
