class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        :note:
            pre列表存储上一行节点，根据pre计算cur列表存储当前行的节点
        """
        rowIndex += 1
        if not rowIndex or rowIndex < 1:
            return None
        pre = cur = [1]
        for i in range(1, rowIndex):
            l = len(pre)
            cur = [1]
            for j in range(l-1):
                cur.append(pre[j]+pre[j+1])
            cur.append(1)
            pre = cur
        return cur
