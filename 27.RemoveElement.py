class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        :note:
            —— 这里是直接删除了，记录删除个数，索引i要减去删除个数
            —— 另一种方法：首尾指针对换数据
        """
        l = len(nums)
        removeNum = 0
        for i in range(l):
            i = i - removeNum
            if nums[i] == val:
                nums.remove(nums[i])
                removeNum += 1
        return l - removeNum
