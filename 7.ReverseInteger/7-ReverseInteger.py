class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        :note:
            首先去符号，以及特殊情况0,以0结尾的
            依次*10 + 余数
            最后添加上符号，以及判断是否溢出
        """
        sign = -1 if x < 0 else 1
        x = -x if x < 0 else x
        if x == 0:
            return 0
        ans = 0
        while(x % 10 == 0):
            x /= 10
        while(x / 10 != 0):
            ans = ans * 10 + x % 10
            x /= 10
            print ans
        ans = ans * 10 + x % 10
        ans *= sign
        if ans > 2**31 - 1 or ans < -2**31:
            return 0
        else:
            return ans
