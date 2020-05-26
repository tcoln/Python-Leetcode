# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        :note:
            1、先统计有多少个节点，得出有多少个group
            2、针对每个group里后面k-1点，更新pre和cur节点
            3、注意记录前一个group的first节点和当前group的first节点：preFirst、first
        """
        if head == None or head.next == None or k <= 0:
            return head
        
        # test have k-th node
        cur = head
        n = 0
        while(cur):
            n += 1
            cur = cur.next
        if n < k:
            return head
        
        # print list for testing   
        def printList(head):
            c = head
            while(c):
                print c.val,
                c = c.next
            print ''
            
        G = n / k
        for g in range(G):
            # reverse k nodes
            if g == 0:
                preFirst = None
                first = pre = head
                cur = head.next
            else:
                first = pre = cur
                cur = cur.next
            for i in range(k-1):
                curNext = cur.next
                cur.next = pre
                pre = cur
                cur =  curNext
            if preFirst:
                preFirst.next = pre
            else:
                head = pre
            preFirst = first
            preFirst.next = None
            printList(head)
        preFirst.next = cur 
        return head
