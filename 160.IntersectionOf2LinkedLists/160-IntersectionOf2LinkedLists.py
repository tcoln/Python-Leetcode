# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        :note:
            长的链表先走一步，跟链表判断环有点相似快慢指针相遇之后的有点相似
        """
        # solution2
        h1, h2 = headA, headB
        if h1 == None or h2 == None:
            return None
        while(h1 != h2):
            h1 = h1.next if h1 != None else headB
            h2 = h2.next if h2 != None else headA
            
        return h1
        
        # solution2
        l1 = l2 = 0
        h1, h2 = headA, headB
        while(h1):
            l1 += 1
            h1 = h1.next
        while(h2):
            l2 += 1
            h2 = h2.next
        
        g = 0
        gap = abs(l2-l1)
        print l1, l2, gap
        h1, h2 = headA, headB
        if l2 > l1:
            while(h2):
                g += 1
                if g > gap:
                    break
                h2 = h2.next
        else:
            while(h1):
                g += 1
                if g > gap:
                    break
                h1 = h1.next
        while(h1 and h2):
            if h1 == h2:
                return h1
            else:
                h1 = h1.next
                h2 = h2.next
        return None
