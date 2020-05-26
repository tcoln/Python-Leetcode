# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        :note:
            跟合并两个有序链表没啥区别，为了节省时间，需要动态删除lists节点，因此需要改用while循环
        """
        #lists[0] = ListNode(1)
        #lists[1] = ListNode(0)
        #lists.pop()
        
        l = len(lists)
        if l == 0:
            return None
        if l == 1:
            return lists[0]
        
        head = pre = None
        while(l > 0):
            minI, minV = -1, float('inf')
            i = 0
            while i < l:
                if lists[i] == None:
                    l -= 1
                    del lists[i]
                    continue
                if lists[i].val < minV:
                    minV = lists[i].val
                    minI = i
                i += 1
            if minI == -1:
                return head
            if head == None:
                head = pre = lists[minI]
            else:
                pre.next = lists[minI]
            pre = lists[minI]
            lists[minI] = lists[minI].next
        return head
