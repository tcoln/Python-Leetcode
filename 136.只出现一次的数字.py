class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :note: 
            异或运算的三大规律：a^0=a, a^a=0, a^a^b=b^a^a
        """
        if not nums:
            return None
        ans = 0
        for num in nums:
            ans = ans ^ num
        return ans
