class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        :note:
            分三步走，首先二分查找判断是否能够找到，然后二分查找target-0.5和target+0.5
        """
        #target = 7
        
        l = len(nums)
        if l == 0:
            return [-1, -1]
        
        start = target - 0.5
        end = target + 0.5
        isFind = self.bsearchPos(nums, target, 1)
        if isFind == -1:
            return [-1, -1]
        else:
            startPos = self.bsearchPos(nums, start, 2)
            endPos = self.bsearchPos(nums, end, 3)
            return [startPos, endPos]
        
    def bsearchPos(self, nums, target, findType):
        # findType = 1 find target, = 2 find start, = 3 find end
        l = len(nums)
        if l == 0:
            return -1
        i, j = 0, l-1
        while(i<=j):
            m = (i+j)/2
            if target > nums[m]:
                i = m+1
            elif target < nums[m]:
                j = m-1
            else:
                return m
        # not find
        if findType == 1:
            return -1
        elif findType == 2:
            return max(i, j)
        else:
            return min(i, j)
