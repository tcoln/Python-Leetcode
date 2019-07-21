class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        :note:
            #1 对区间按起点start排序，然后一次遍历更新就行了
            #2 暴力遍历对于每个区间i，遍历剩下的所有区间并用合并后区间代替原区间。
            时间O(n^2)，这是对于排序后的，若没有排序则需要遍历除了i所有区间。
        """
        #intervals = [[1,4],[0,2],[3,5]]
        if not intervals or len(intervals) < 1:
            return None
        intervals.sort(key=lambda item:item[0])
        i = 1
        l = len(intervals)
        while i < l:
            pre = intervals[i-1]
            item = intervals[i]
            if item[0] <= pre[1]:
                if item[1] > pre[1]:
                    pre[1] = item[1]
                del intervals[i]
                l -= 1
            else:
                i += 1
        return intervals
