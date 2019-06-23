class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        :note:
            堆排序然后返回倒数第k个数
            堆排序分两步，第一步，依次从倒数第一个父节点建堆，建好后最大值堆顶交换到最后一个位置，注意这里建堆的时候如果交换了子节点，需要递归的在孩子节点上继续建堆。
                         第二步，每次都从根节点开始向下建堆，建好后最大值堆顶交换到倒数的位置上
        """
        #nums, k = [3,2,3,1,2,4,5,5,6], 4
        
        def heapsort(nums):
            l = len(nums)
            # build heap
            for i in range(l/2-1, -1, -1):
                heapify(nums, i, l)
            #print 'build ', nums
            # swap and heapify
            for i in range(l-1, 0, -1):
                nums[0], nums[i] = nums[i], nums[0]
                heapify(nums, 0, i)
            print 'sorted ', nums
        
        def heapify(nums, root, size):
            #print nums, root
            maxi = root
            left = 2 * root + 1
            right = 2 * root + 2
            if left < size and nums[maxi] < nums[left]:
                maxi = left
            if right < size and nums[maxi] < nums[right]:
                maxi = right
            if maxi != root:
                nums[root], nums[maxi] = nums[maxi], nums[root]
                heapify(nums, maxi, size)
        
        def heapify_no_recursive(nums, root, size):
            while True:
                maxi = root
                left = 2 * root + 1
                right = 2 * root + 2
                if left >= size:
                    break
                if left < size and nums[maxi] < nums[left]:
                    maxi = left
                if right < size and nums[maxi] < nums[right]:
                    maxi = right
                if maxi != root:
                    nums[root], nums[maxi] = nums[maxi], nums[root]
                    root = maxi
                else:
                    break
                
        heapsort(nums)
        return nums[-k]
        
