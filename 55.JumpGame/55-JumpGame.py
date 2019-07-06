class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        :note:
            依次遍历reachable的位置，更新能够reachable的最远端位置
        """
        #nums = [3,2,1,0,4]
        l = len(nums)
        i = reachable = 0
        while(i < l and reachable >= i):
            if i + nums[i] > reachable:
                reachable = i + nums[i]
            i += 1
        if reachable >= l-1:
            return True
        else:
            return False
