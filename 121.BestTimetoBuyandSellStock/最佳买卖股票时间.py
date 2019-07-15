class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        :note:
            记录截止**前一天**的最小价格，如果今天的收益更大则更新最大的收益
            如果今天的价格比最小价格还小则更新最小价格，为下一次计算做准备
        """
        if prices == None:
            return 0
        l = len(prices)
        if l == 1:
            return 0
        minp = float('inf')
        maxProfit = 0
        for i in range(l):
            if prices[i] - minp > maxProfit:
                maxProfit = prices[i] - minp
            if prices[i] < minp:
                minp = prices[i]
        return maxProfit
