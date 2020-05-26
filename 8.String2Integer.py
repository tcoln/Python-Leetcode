class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        :note:
            主要是要判断正负号以及数字后面如果有字符是否为数字
        """
        #s = 'sdfsdf    -42 safasfsf'
        l = len(s)
        sign = 1
        ans = 0
        for i in range(l):
            if s[i] == ' ':
                continue
            if s[i] == '-':
                sign = -1
                if i + 1 < l and s[i+1] >= '0' and s[i+1] <= '9':
                    continue
                else:
                    break
            if s[i] == '+':
                if i + 1 < l and s[i+1] >= '0' and s[i+1] <= '9':
                    continue
                else:
                    break
            if s[i] > '9' or s[i] < '0':
                break
            else:
                ans = ans * 10 + int(s[i])
                if i + 1 < l and s[i+1] >= '0' and s[i+1] <= '9':
                    continue
                else:
                    break
        ans =  ans*sign
        if ans > 2**31 - 1:
            ans = 2**31 - 1
        if ans < -2**31:
            ans = -2**31
        return ans
