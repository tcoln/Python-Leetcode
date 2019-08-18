class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        :note:
            用另外一个栈存储截止目前最小的元素
        """
        self.sdata = []
        self.mindata = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.sdata.append(x)
        m = x if not self.mindata else min(x, self.getMin())
        self.mindata.append(m)

    def pop(self):
        """
        :rtype: None
        """
        del self.sdata[-1]
        del self.mindata[-1]
        
    def top(self):
        """
        :rtype: int
        """
        return self.sdata[-1]    

    def getMin(self):
        """
        :rtype: int
        """
        #print self.sdata, self.mindata
        return self.mindata[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
