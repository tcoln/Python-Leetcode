class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        :note:
            分两步走：首先从后往前遍历i，找到i后面比i 大 且 最小数minJ，交换i和minJ；然后将i后面的数升序排序
        """
        #nums = [2,3,1]
        #nums = [3,2,1]
        
        l = len(nums)
        for i in range(l-2, -1, -1):
            minJ, minN = -1, float('Inf')
            for j in range(i+1, l):
                if nums[j] > nums[i] and nums[j] < minN:
                    minJ = j
                    minN = nums[j]
            #print nums[i],  minN
            if minJ != -1:
                nums[i], nums[minJ] = nums[minJ], nums[i]
                tmp = nums[i+1:]
                tmp.sort()
                nums[i+1:] = tmp
                print nums
                return
        nums.sort()
        
        print nums
