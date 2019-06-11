class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        :nonte:
            执行二分查找，当找不到的时候(i>j)，分为三种情况：
                —— i上溢出了
                —— j下溢出了
                —— 当i在数组中间，分两种情况返回位置
        """
        #target = 2
        
        l = len(nums)
        if l == 0:
            return 0
        
        i, j = 0, l - 1
        while(i <= j):
            m = (i+j)/2
            if target > nums[m]:
                i = m + 1
            elif target < nums[m]:
                j = m - 1
            else:
                return m
        if i > l-1:
            return l
        if j < 0:
            return 0
        if target > nums[i]:
            return i+1
        else:
            return i
