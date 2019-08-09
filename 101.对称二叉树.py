# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        :note:
            对称二叉树的左右子树前序遍历近似（先左还是先右）相等
        """
        if not root:
            return True  
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        if root.left.val != root.right.val:
            return False
        
        def preOrder(r, flag):
            if not r:
                return [None]
            ans = [r.val]
            if flag == 'l':
                ans.extend(preOrder(r.left, 'l'))
                ans.extend(preOrder(r.right, 'r'))
            else:
                ans.extend(preOrder(r.right, 'r'))
                ans.extend(preOrder(r.left, 'l'))
            return ans
        
        return preOrder(root.left, 'l') == preOrder(root.right, 'r')
