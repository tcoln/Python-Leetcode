class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        :note:
            两遍：统计不同颜色球的个数，然后根据个数填值
            一遍：维护三个颜色球的指针i,j,k，当前位置k不管先置为2，如果是小于2，j置为1（2给了个1），如果是0，i置为0（1给了个0）。
        """
        l = len(nums)
        # one pass
        i = j = k =0
        for k in range(l):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1
        return        
        
        # two pass
        n0 = n1 = n2 = 0
        for i in nums:
            if i == 0:
                n0 += 1
            elif i == 1:
                n1 += 1
            else:
                n2 += 1
        for i in range(n0):
            nums[i] = 0
        for i in range(n0, n0+n1):
            nums[i] = 1
        for i in range(n0+n1, n0+n1+n2):
            nums[i] = 2
