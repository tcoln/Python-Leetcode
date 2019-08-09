from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        :note:
            队列层次遍历，记录当前层节点数和下一层的节点数，队列操作时及时更新
        """
        if not root:
            return []
        q = deque([root])
        curl = 1
        nextl = 0
        layer = []
        ans = []
        while q:
            cur = q.pop()
            layer.append(cur.val)
            if cur.left:
                q.appendleft(cur.left)
                nextl += 1
            if cur.right:
                q.appendleft(cur.right)
                nextl += 1
            curl -= 1
            if curl == 0:
                curl = nextl
                nextl = 0
                #print layer
                ans.append(layer)
                layer = []
        return ans
