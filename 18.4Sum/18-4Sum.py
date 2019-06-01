class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        :note:
            类似3sum，排序，两层遍历，循环搜索起点、终点。
            但是要注意前三层循环的时候遇到重复值时，要跳过。
        """
        #nums = [-3,-4,-5,0,-5,-2,5,2,-3]
        #target = 3

        l = len(nums)
        ans = []
        if l < 4:
            return ans
        nums.sort()
        print nums
        i = 0
        while(i < l-3): #for i in range(l-3):   同下
            while(nums[i] == nums[i-1] and i > 0):
                i += 1
            print i
            j = i+1
            while(j < l-2): #用for循环的话，在循环体里改变不了下一次循环的j值
                while(nums[j] == nums[j-1] and j < l-2 and j > i+1):
                            j += 1
                s, e = j+1, l-1
                while(s < e):
                    fsum = nums[i] + nums[j] + nums[s] + nums[e]
                    if fsum == target:
                        ans.append([nums[i], nums[j], nums[s], nums[e]])
                        s += 1
                        while(nums[s] == nums[s-1] and s < e):
                            s += 1
                    elif fsum < target:
                        s += 1
                    else:
                        e -= 1
                j += 1
            i += 1
        return ans
