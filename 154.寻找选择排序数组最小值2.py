class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :note:
            中间元素跟最后一个元素比，有大于、小于、等于三种情况
            大于好办，小于要包含中间元素（eg:[3,1,2],因为是求最小元素，m小于肯定得包含m）
            等于情况就比较复杂了，可以 right -= 1
        """
        if not nums:
                return 
        l = len(nums)
        if l == 1:
            return nums[0]
        left, right = 0, l-1
        while left < right:
            m = (left+right)/2
            if nums[m] > nums[right]:
                left = m + 1
            elif nums[m] < nums[right]:
                right = m
            else:
                right = right - 1
        return nums[left]
        
        #return min(nums)
