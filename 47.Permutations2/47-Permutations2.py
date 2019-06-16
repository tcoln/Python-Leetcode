class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        :note:
            回溯法中序遍历排列树，有三点需要注意：
            1、list浅复制
            2、遍历下一层的时候remove已经使用过的数字
            3、遍历下一层的时候set去重
        """
        #nums=[1,1,1,2]
        
        l = len(nums)
        ans = []
        
        def InOrder(per):
            if len(per) == l:
                ans.append(list(per))
                return
            remain = list(nums)
            for num in per:
                remain.remove(num)
            for num in set(remain):
                per.append(num)
                InOrder(per)
                per.pop()
                
        InOrder([])
        return ans
