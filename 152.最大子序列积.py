class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :note:
            类似于最大子序列和，求以当前元素结尾的最大积。
            但是记录两个数组，分别是当前元素结尾的最大积和最小积，
            负数的时候最小值是与最大值求积，最大值是与最小值求积。
   	美团面试大佬问了，为啥不O(1)空间复杂度     
	"""
	if not nums:
            return 0
        l = len(nums)
        ans = maxp = minp = nums[0]
        for i in range(1, l):
            print maxp, minp
            if nums[i] >= 0:
                maxp = max(maxp * nums[i], nums[i])
                minp = min(minp * nums[i], nums[i])
            else:
                tmp = maxp
                maxp = max(minp * nums[i], nums[i])
                minp = min(tmp * nums[i], nums[i])
            ans = max(ans, maxp)
        return ans
    
        #1 暴力方法
        if not nums:
            return 0
        l = len(nums)
        ans = nums[0]
        for i in range(1, l):
            maxp = 1
            for j in range(i, -1, -1):
                maxp *= nums[j] 
                if maxp > ans:
                    ans = maxp
                print maxp
        return ans
