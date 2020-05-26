class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        l = len(s)
        rs = ''
        for i in range(l):
            rs = s[i] + rs
        ans = True if s == rs else False
        return ans
