class Solution(object):
     
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        :note:
            递归的统计前一项字符串中的数字个数；
            为了节省时间，用打表法记录当前的解；或者像斐波那契数列那样循环往前计算
        """
        #n = 10
        
        self.table = [None for i in range(31)]
        self.count(n, self.table)
        return self.table[n]
        
    def count(self, n, table):
        if n == 1:
            self.table[n] = '1'
            return self.table[n]
        else:
            if self.table[n] == None:
                self.count(n-1, self.table)
                s = self.table[n-1]
                #print s
                l = len(s)
                sNext = ''
                count = 1
                for i in range(1, l):
                    if s[i] == s[i-1]:
                        count += 1
                    else:
                        sNext += str(count) + s[i-1]
                        count = 1
                sNext += str(count) + s[l-1]
                self.table[n] = sNext
            else:
                return self.table[n]
