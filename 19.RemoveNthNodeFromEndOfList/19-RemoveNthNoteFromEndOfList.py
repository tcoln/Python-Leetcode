# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        :note:
            两个节点指针，后面一个隔着前一个n个节点追着跑。注意边界值检测。
        """
        #head = ListNode(1)
        #head.next = ListNode(2)
        #n = 1
        
        p1 = p2 = head
        for i in range(n):
            if p2 == None:
                return head
            p2 = p2.next
        print p1.val, p2
        if p2 == None:
            head = p1.next
            return head
        while(p2.next != None):
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return head
