class Solution(object):
    def __init__(self):
        self.alpha = 'abcdefghijklmnopqrstuvwxyz'
    
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        :note:
            递归的实现，当前数字的字母们与后面剩下数字的字母列表们进行组合
            注意递归返回的是字母组合的列表
        """
        #digits = '3'
        a = self.num2letter(digits)
        return a
    
    def num2letter(self, nums):
        ans = []
        l = len(nums)
        if l == 0:
            return ''
        n = int(nums[0])
        nStr = 'wxyz'
        if n == 8:
            nStr = 'tuv'
        if n == 7:
            nStr = 'pqrs'
        if n < 7:
            nStr = self.alpha[(n-2)*3:(n-1)*3]
        for i in nStr:
            post =  self.num2letter(nums[1:])
            if post != '':
                for j in post:
                    ans.append(i + j)
            else:
                ans.append(i)
        #print nStr, ans
        return ans
