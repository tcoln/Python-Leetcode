import random

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        :note:
            蓄水池算法，先蓄好k个水，然后依次从k+1遍历，并判断生成的randint(0,k)是否在蓄水池内(<k)
            注:Python的randint(a,b)是包含a和b的
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        ans = self.head
        cur = self.head.next
        i = 1
        while(cur):
            r = random.randint(0, i)
            if r == 0:
                ans = cur
            cur = cur.next
            i += 1
        return ans.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
