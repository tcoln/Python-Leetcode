class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        :note:
            1、去符号
            2、移位操作 ret = a0*2^0 + a1*2^1 + ...... + a30*2^30 + a31*2^31; ai = 0 or 1, i = 0......31 
            3、加符号
            4、溢出处理
        """
        #dividend, divisor= 2147483647, 3
        #dividend, divisor= 1000, 3
        
        # remove sign
        D = abs(dividend)
        d = abs(divisor)
        
        # 移位操作
        times = 0
        print bin(dividend/divisor)
        for i in range(31, -1, -1):  
            #print bin(D>>i)
            if D >> i >= d:
                times += 1 << i
                D = D - (d<<i);
                #D = D - times
                print i, 1 << i, times, D
        
        # add sign
        if dividend < 0:
            times = -times
        if divisor < 0:
            times = -times
        
        # overflow
        if times < -2**31 or times > 2**31-1:
            times = 2**31-1
            
        return times
