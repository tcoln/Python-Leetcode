from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        :note:
            标记奇偶层号，直接反转layer
        """
        if not root:
            return []
        q = deque([root])
        curl = 1
        nextl = 0
        layerNum = 1
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
                #print layer, layerNum
                curl = nextl
                nextl = 0
                if layerNum % 2 == 0:
                    layer.reverse()
                ans.append(layer)
                layerNum += 1
                layer = []
        return ans
