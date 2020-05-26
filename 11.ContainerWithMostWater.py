class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        :note:
            双指针夹逼法
        """
        #height = [2,3,10,5,7,8,9]
        
        l = len(height)
        i, j = 0, l-1
        maxWater = 0
        while(i != j):
            water = min(height[i], height[j]) * (j-i)
            if water > maxWater:
                maxWater = water
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxWater
