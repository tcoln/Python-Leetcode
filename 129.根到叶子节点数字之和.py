# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        :note:  
            先序遍历，回溯法
        """
        global ans
        ans = 0
        def preOrder(r, pre):
            global ans
            if not r:
                return
            if not r.left and not r.right:
                ans += 10*pre + r.val
                return
            preOrder(r.left, pre*10+r.val)
            preOrder(r.right, pre*10+r.val)
            return ans
        preOrder(root, 0)
        return ans
