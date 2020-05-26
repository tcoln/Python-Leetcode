class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        :note:
            使用常规的排序算法，但是交换条件需要自定义。这里使用插入排序。
            第一种方法：循环的找到数字中某一位数字要大的那个数字进行交换。
            第二种方法：根据str(x)+str(y)>str(y)+str(x)来交换。            
        """
        #nums = [3,30,34,5,9]
        #nums = [121, 12]
        #nums = [0,0]
        #nums = [1, 11]
        #nums = [824,938,1399,5607,6973,5703,9609,4398,8247]
        
        l = len(nums)
        # insert sort
        for i in range(1, l):
            tmp = nums[i]
            pos = i
            for j in range(i-1, -1, -1):
                # recycle find first diff digit
                index1 = index2 = 0
                m, n = str(tmp)[index1], str(nums[j])[index2]
                ltmp = len(str(tmp))
                lnumj = len(str(nums[j]))
                times = 0
                while(m == n):
                    index1 += 1
                    index2 += 1
                    if index1 >= ltmp:
                        index1 = 0
                        times += 1
                    m = str(tmp)[index1]
                    if index2 >= lnumj:
                        index2 = 0
                        times += 1
                    n = str(nums[j])[index2]
                    if times >= 2:
                        break
                 
                # x+y > y+x
                n = nums[j]
                # print m, n, nums
                if str(tmp)+str(n) > str(n)+str(tmp):
                    nums[j+1] = nums[j]
                    pos = j                    
                else:
                    break
            nums[pos] = tmp
            
        if nums[0] == 0:
            return '0'
        largestNum = ''
        for i in nums:
            largestNum += str(i)
        print nums, largestNum
        return largestNum
        
        # insert sort
        def insertsort(nums, l):
            for i in range(1, l):
                tmp = nums[i]
                pos = i
                for j in range(i-1, -1, -1):
                    if tmp > nums[j]:
                        nums[j+1] = nums[j]
                        pos = j
                    else:
                        break
                nums[pos] = tmp     
