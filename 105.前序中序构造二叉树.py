# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        :note:
            切割先序和中序序列，递归的构造左右子树
        """
        if not preorder:
            return None
        rval = preorder[0]
        rindex = inorder.index(rval)
        lin = inorder[:rindex]
        rin = inorder[rindex+1:]
        lpre = preorder[1:1+len(lin)]
        rpre = preorder[len(lin)+1:]
        root = TreeNode(rval)
        root.left = self.buildTree(lpre, lin)
        root.right = self.buildTree(rpre, rin)
        return root
