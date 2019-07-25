# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        :note:
            递归的flatten左右子树，如果左子树存在则将左子树插入到右子树前面，用pre存储左子树的最后一个节点来拼接
        """
        if not root:
            return
        if not root.left and not root.right:
            return
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        # get last node
        pre = root.left
        cur = root.left
        while(cur):
            pre = cur
            cur = cur.right
            
        if pre:
            tmp = root.right
            root.right = root.left
            root.left = None
            pre.right = tmp
