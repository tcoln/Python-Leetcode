ass Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        :note:
            分两步走：1、第一步log(n)时间找到旋转点i,j；2、第二步分布在旋转点两侧二分查找；总共是3个log(n)时间
            注意：
                    —— 当数组没有旋转时：要么只有两个元素，要么i==j，则直接二分查找
                    —— 当在后半旋转部分查找时，记得索引+j
                    
            升级版的二分查找
        """
        #nums = [4,5]
        #target = 5
        
        # solution2
        
        n = len(nums)
        l, r = 0, n-1
        while(l <= r):
            m = (l+r)/2
            if nums[m] == target:
                return m
            elif nums[m] < nums[r]:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
        
        
        
        
        # solution 1
        
        # special case
        l = len(nums)
        if nums == []:
            return -1
        if l == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        if l==2 and nums[0] < nums[1]:
                return self.bsearch(nums, target)
            
        # find rotate point i, j
        i, j = 0, l-1
        while(i != j - 1):
            m = (i+j)/2
            if nums[m] > nums[i]:
                i = m
            if nums[m] < nums[j]:
                j = m
            if i == j:
                return self.bsearch(nums, target)
        print i, j  
        
        # search half nums
        if target < nums[0]:
            ans =  self.bsearch(nums[j:], target)
            if ans == -1:
                return ans
            else:
                return ans + j
        else:
            return self.bsearch(nums[:i+1], target)
        
    # binary search
    def bsearch(self, nums, target):
        l = len(nums)
        i, j = 0, l-1
        while(i<=j):
            m = (i + j)/2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                i = m+1
            else:
                j = m-1
        return -1
