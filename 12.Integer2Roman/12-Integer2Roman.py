class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        :note:
            先建立两个数组存储对应的字典；
            然后精准匹配当前数字的条件，排除9开头的数字
            注意，当匹配数字以5开头的时候，要跟它前一个数字进行匹配
        """
        #num = 3
        number = [1, 5, 10, 50, 100, 500, 1000]
        symbol = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        l = len(number)
        ans = ''
        for i in range(l-1, -1, -1):
            #print ans, num, str(num)[0]
            n = number[i]
            s = symbol[i]
            a = num / n
            if a > 0 and a < 4 and str(num)[0] != '9':
                for j in range(a):
                    ans += s
                num %= n
                continue
            if str(n)[0] == '5' and num / number[i-1] == 9:
                ans += (symbol[i-1] + symbol[i+1])
                num -= 9 * number[i-1]
                continue
            if str(n)[0] == '5' and num / number[i-1] == 4:
                ans += (symbol[i-1] + symbol[i])
                num -= 4 * number[i-1]
                continue      
        return ans
