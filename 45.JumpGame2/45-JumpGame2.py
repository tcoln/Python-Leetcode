class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :note:
            从前往后遍历，更新当前节点能够reachable的最远端的位置，同时更新reachable范围内的steps
        """
        #nums = [2,1]
        
        # solution1 贪心
        reachable = 0
        l = len(nums)
        steps = [float('inf') for i in range(l)]
        steps[0] = 0
        i = 0
        while(i <= reachable):
            if reachable >= l-1:
                break
            if i + nums[i] > reachable:
                reachable = i + nums[i]
                for j in range(i+1, i+nums[i]+1):
                    if j < l and steps[i] + 1 < steps[j]:
                        steps[j] = steps[i]+1
            i += 1
        return steps[-1]
    
        # solution2 反序遍历+动态规划 minJump[i] = minJump[i+1 : i+nums[i]+1] + 1，注意nums[i]==0 (i!=l-1)不能跳
        l = len(nums)
        minJump = [0 for i in range(l)]
        for i in range(l-2, -1, -1):
            if nums[i] == 0:
                minJump[i] = 0
            else:
                minI = float('inf')
                for j in range(i+1, i+nums[i]+1):
                    if j == l-1:
                        minI = 0
                    elif j < l and minJump[j] != 0 and minJump[j] < minI:
                        minI = minJump[j]
                minJump[i] = minI + 1
        return minJump[0]
