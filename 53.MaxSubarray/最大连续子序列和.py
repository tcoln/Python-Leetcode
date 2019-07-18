class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :note:
            记录以当前位置为结尾的最大连续子序列和，DP的更新下一个
        """
        if nums == None:
            return 0
        if len(nums) == 1:
            return nums[0]
        l = len(nums)
        maxL = [nums[0] for i in range(l)]
        for i in range(1, l):
            if maxL[i-1] > 0:
                maxL[i] = maxL[i-1] + nums[i]
            else:
                maxL[i] = nums[i]
        return max(maxL)
