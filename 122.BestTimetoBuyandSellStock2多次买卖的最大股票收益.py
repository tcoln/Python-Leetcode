class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        :note:
            上一题用DP算法，本题用贪心算法，只有今天有收益就买卖
        """
        if prices == None or len(prices) == 1:
            return 0
        l = len(prices)
        maxProfit = 0
        for i in range(1, l):
            if prices[i] - prices[i-1] > 0:
                maxProfit += prices[i] - prices[i-1]
        return maxProfit
