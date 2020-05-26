class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        ：note:
            移动左右指针中值较小的，每移动一次，如果变低了，则累加左右指针中最小值 与 当前值得差值水位
        """
        if height == None or len(height) < 1:
            return 0
        l = len(height)
        i, j = 0, l-1
        lmax, rmax = height[i], height[j]
        ans = 0
        while(i < j):
            if height[i] <= height[j]:
                i += 1
                if height[i] < lmax:
                    ans += lmax - height[i]
                else:
                    lmax = height[i]
            else:
                j -= 1
                if height[j] < rmax:
                    ans +=  rmax - height[j]
                else:
                    rmax = height[j]
        return ans
