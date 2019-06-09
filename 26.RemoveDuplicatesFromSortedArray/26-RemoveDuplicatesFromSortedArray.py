class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :note:
            考察数组的引用。
            每次删掉一个重复值，循环的时候i要减去删掉的个数
        """
        l = len(nums)
        dnums = 0
        for i in range(l-1):
            i = i - dnums
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])
                dnums += 1
            #print nums
        return l-dnums
