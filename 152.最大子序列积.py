class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :note:
            类似于最大子序列和，求以当前元素结尾的最大积。
            但是记录两个数组，分别是当前元素结尾的最大积和最小积，
            负数的时候最小值是与最大值求积，最大值是与最小值求积。
        """
        #nums = [-2, 0, -1]
        if not nums:
            return 0
        l = len(nums)
        #2 DP
        maxp = [i for i in nums]
        minp = [i for i in nums]
        for i in range(1, l):
            if nums[i] >= 0:
                maxp[i] = max(maxp[i-1] * nums[i], nums[i])
                minp[i] = min(minp[i-1] * nums[i], nums[i])
            else:
                maxp[i] = max(minp[i-1] * nums[i], nums[i])
                minp[i] = min(maxp[i-1] * nums[i], nums[i])
        print maxp      
        return max(maxp)
    
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
