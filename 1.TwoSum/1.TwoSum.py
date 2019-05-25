class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        comdict = dict()
        n = len(nums)
        for i in range(n):
            comple = target - nums[i]
            comdict[comple] = i
        for i in range(n-1, -1,-1):
            if comdict.has_key(nums[i]) and comdict[nums[i]] != i:
                    return [comdict[nums[i]], i]
