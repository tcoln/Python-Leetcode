# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        :note:
            合并有序列表
        """
        #l1 = l2 = None
        new = pre = None
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        while(l1 != None and l2 != None):
            v1 = l1.val
            v2 = l2.val
            if v1 <= v2:
                if pre == None:
                    new = pre = l1
                else:
                    pre.next = l1
                    pre = l1
                l1 = l1.next
            else:
                if pre == None:
                    new = pre = l2
                else:
                    pre.next = l2
                    pre = l2
                l2 = l2.next
        if l1 == None:
            pre.next = l2
        else:
            pre.next = l1
        return new
        
