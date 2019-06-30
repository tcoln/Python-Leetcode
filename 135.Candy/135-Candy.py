class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        :note:
            先从左往右扫描，保证右边的如果比左边得分的大，则等于左边的糖果数+1；
            然后从右往左扫描，保证如果左边的得分比右边的大，且糖果比右边的+1少，则等于右边的糖果数+1
        """
        l = len(ratings)
        candys = [1 for i in range(l)]
        for i in range(1, l):
            if ratings[i] > ratings[i-1]:
                candys[i] = candys[i-1] + 1
        for i in range(l-2, -1, -1):
            if ratings[i] > ratings[i+1] and candys[i] < candys[i+1]+1:
                candys[i] = candys[i+1] + 1
        return sum(candys)
