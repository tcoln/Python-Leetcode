class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        note:
            用hashset存储nums
            第一步找到所有的起点（num-1不在nums中）
            第二步对所有的起点遍历num+1，在的话继续+1，不在的话更新maxL
        """
        if not nums:
            return 0
        numset = set(nums)
        maxl = 1
        for num in nums:
            if num-1 not in numset: #是起点
                l = 1
                while num+1 in numset:
                    l += 1
                    num += 1
                maxl = max(l, maxl)
        return maxl
