import bisect as bi
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :note:
            中间元素跟最后一个元素比，有大于、小于、等于三种情况
            大于好办，小于要包含中间元素（eg:[3,1,2],因为是求最小元素，m小于肯定得包含m），等于只有len==2的情况。
        """
        if not nums:
                return 
        l = len(nums)
        if l == 1:
            return nums[0]

        def getMin(nums):
            print nums
            l = len(nums)
            if l == 1:
                return nums[0]
            m = nums[l/2]
            if m > nums[-1]:
                return getMin(nums[l/2+1:])
            elif m < nums[-1]:
                return getMin(nums[:l/2+1])
            else:
                return min(nums[0], m)
        return getMin(nums)
        
        #return min(nums)
