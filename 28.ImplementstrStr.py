class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        :note:
            暴力搜索
        """
        ln = len(needle)
        lh = len(haystack)
        if ln == 0 or needle == None:
            return 0
        for i in range(lh-ln+1):
            if haystack[i:i+ln] == needle:
                return i
        return -1
