class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
	:note:第一轮用字典存储每个数的补数, 第二轮判断数字是否在补数字典中，并且当前索引i不等于补数的索引
        """
        comdict = dict()
        n = len(nums)
        for i in range(n):
            comple = target - nums[i]
            comdict[comple] = i
        for i in range(n-1, -1,-1):
            if comdict.has_key(nums[i]) and comdict[nums[i]] != i:
                    return [comdict[nums[i]], i]
