# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        :note:
            递归的判断每个节点是否满足平衡条件，abs(leftH - rightH) <= 1
            平衡二叉树的定义是：当前节点满足，且左右子树也满足
        """
        if not root:
            return True
        
        def isBST(r):
            if r == None:
                return True
            lH = getH(r.left)
            rH = getH(r.right)
            if abs(lH-rH) <= 1 and isBST(r.left) and isBST(r.right):
                return True
            return False
        
        # 求树高
        def getH(r):
            if not r:
                return 0
            return max(getH(r.left), getH(r.right)) + 1
        
        return isBST(root)
