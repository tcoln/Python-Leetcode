# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = l1.val
        num2 = l2.val
        rank = 10
        while(l1.next != None):
            l1 = l1.next
            num1 += l1.val *  rank
            rank *= 10
        rank = 10
        while(l2.next != None):
            l2 = l2.next
            num2 += l2.val * rank
            rank *= 10
        num = num1 + num2
        L = pre = None
        if num == 0:
            L = ListNode(0)
            return L
        while(num != 0):
            cur = ListNode(num % 10)
            num /= 10
            if pre != None:
                pre.next = cur
                pre = cur
            else :
                L = pre = cur
        return L
