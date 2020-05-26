# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        :note:
            定义三个节点：pre、cur、curNext，先交换cur和curNext，然后更新和移动pre节点。
        """
            
        def printList(head):
            while(head):
                print head.val,
                head = head.next
            print ''
                
        if head == None or head.next == None:
            return head          
        pre = None
        cur = head
        curNext = cur.next
        while(True):
            print pre if pre==None else pre.val, cur.val, curNext.val
            printList(head)
            if pre == None:
                head = curNext
                cur.next = curNext.next
                curNext.next = cur
                pre = cur
            else:
                cur.next = curNext.next
                curNext.next = cur
                pre.next = curNext
                pre = cur
            printList(head)
            if cur.next == None or cur.next.next == None:
                break
            cur = cur.next
            curNext = cur.next
        return head
