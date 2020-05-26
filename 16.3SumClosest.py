class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        :note:
            借鉴3sum的思想，先将nums排序，然后遍历第一个元素，以及后面的s和e，及时更新最近距离，然后跟target比较：小升s,大降e
            注意当等于target的时候提前结束。
        """
        #nums = [1,1,-1,-1,3]
        #target = -1

        nums.sort()
        l = len(nums)
        closest = float('inf')
        ans = 0
        for i in range(l-2):
            s, e = i+1, l-1
            while s < e:
                #print i, s, e
                c = abs(target - (nums[i] + nums[s] + nums[e]))
                #print c, c < closest, nums[i],nums[s], nums[e]
                if c == 0:
                    return nums[i] + nums[s] + nums[e]
                if c < closest:
                    closest = c
                    ans = nums[i] + nums[s] + nums[e]
                if target > (nums[i] + nums[s] + nums[e]):
                    s += 1
                if target < (nums[i] + nums[s] + nums[e]):
                    e -= 1
        return ans     
