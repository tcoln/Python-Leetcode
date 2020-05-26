class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        :note:
            回溯法中序遍历排列树，注意list的浅拷贝，以及遍历下一层节点的时候要去掉已经使用过的点。
        """
        
        l = len(nums)
        ans = []
        
        def permu(per):
            if len(per) == l:
                ans.append(list(per))
                return
            for num in nums:
                if num not in per:
                    per.append(num)
                    permu(per)
                    per.pop()
        
        permu([])
        return ans
