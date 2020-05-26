class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        :note:
            有点递归的意思，利用之前计算过的值的平方，幂指数减少一半
            a**b == (a**2)**(b/2),要分奇偶数
        """
        #x, n = 1.72777, 7

        ans = 1
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n
        x1 = 1
        x2 = x
        while n > 1:
            if n % 2 == 1:
                x1 = x1 * x2
                n -= 1
                if n == 0:
                    break
            x2 = x2 * x2
            n = n >> 1 
            #print x2, n, ans
        return x1 * x2
