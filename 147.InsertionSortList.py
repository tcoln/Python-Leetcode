# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        :note:
            插入排序，跟数组不一样，从前往后找插入位置，需要记录插前、插入节点的位置以及当前和前一个节点位置
        """ 
        #head = ListNode(-1)
        #head.next = ListNode(5)
        #head.next.next = ListNode(3)        
        #head.next.next.next = ListNode(4)
        #head.next.next.next.next = ListNode(0)
        
        pref = None
        first = head
        if head == None:
            return head
        prec = head
        cur = head.next
        while(cur):
            while(cur.val >= first.val):
                pref = first
                first = first.next
                if first == cur:
                    break
                    
            curNext = cur.next
            if first != cur: # swap
                #print pref.val, first.val, prec.val, cur.val 
                if pref == None:
                    head = cur
                else:
                    pref.next = cur
                cur.next = first
                prec.next = curNext
            else:
                prec = cur
            
            pref = None
            first = head
            cur = curNext
            #self.printL(head)
        return head
    
    def printL(self, head):
        while(head):
            print head.val,
            head = head.next
        print ''
