class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        :note:
            #1 根据start找到合适位置插入使得依然有序；然后根据56题合并区间
            
            #2
            第一步找到第一个相交或包含的区间：
            遍历intervals每个区间i，判断i与newIntervals的关系，分三种情况
            不想交，直接忽略
            相交，更新i为并集，分左相交和右相交
            包含，更新i
            第二步，遍历合并后面的区间，应用56题合并算法
        """
        #intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        #newInterval = [4,8]
        intervals = [[1,5]]
        newInterval = [0,5]
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
        
        # 插入
        
        
        
        
        
        
        #2
        l = len(intervals)
        for i in range(l):
            item = intervals[i]
            if i == 0 and item[0] > newInterval[1]:
                intervals.insert(0, newInterval)   # 添加到第一个元素
                break
            elif item[0] <= newInterval[0] and item[1] >= newInterval[0] and item[1] <= newInterval[1]:
                item[1] = newInterval[1]    # 左相交
                break
            elif item[0] >= newInterval[0] and item[1] <= newInterval[1]:
                intervals[i] = newInterval # 包含
                #print '包含', item, intervals
                break
            elif item[0] > newInterval[0] and item[0] <= newInterval[1] and item[1] > newInterval[1]:
                item[0] = newInterval[0]    # 右相交
                break
            elif newInterval[0] >= item[0] and newInterval[1] <= item[1]:
                return intervals    # 反包含
            elif i == l-1:
                intervals.append(newInterval)   # 添加到最后一个元素
            
        # 合并区间
        j = i+1 
        #print intervals, j
        while j < l:
            pre = intervals[j-1]
            item = intervals[j]
            if item[0] <= pre[1]:
                if pre[1] < item[1]:
                    pre[1] = item[1]
                del intervals[j]
                j -= 1
                l -= 1
            j += 1
        intervals.sort()
        return intervals
