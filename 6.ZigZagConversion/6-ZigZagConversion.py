class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #numRows = 4
        l = len(s)
        if numRows == 1:
            return s
        a = ''
        for i in range(numRows):
            j = i
            step = 0 if i != numRows-1 else 1
            while(j < l):    
                a += s[j]
                if step % 2 == 0:
                    if i == 0:
                        step += 1
                    down = numRows - (i+1)
                    up = numRows - (i+1)
                    j += down + up
                else:
                    if i == numRows-1:
                        step += 1
                    up = i
                    down = i
                    j += up + down
                step += 1
        return a 
