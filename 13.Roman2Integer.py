class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        :note:
            依次按照字典值相加，若当前字符对应的值比前一个字符对应的字符大，则减去double个这个值。
        """
        #s = 'IV'
        ans = 0
        l = len(s)
        number = [1, 5, 10, 50, 100, 500, 1000]
        symbol = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        preN = float('Inf')
        for i in range(l):
            cur = s[i]
            cur_I = symbol.index(cur)
            n = number[cur_I]
            ans += n
            if n > preN:
                  ans -= 2 * preN
            preN = n
        return ans
