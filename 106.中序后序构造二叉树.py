# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        :note:
            切割先序和中序序列，递归的构造左右子树
        """
        if not postorder:
            return None
        #print inorder, postorder
        rval = postorder[-1]
        rindex = inorder.index(rval)
        lin = inorder[:rindex]
        rin = inorder[rindex+1:]
        lpos = postorder[:len(lin)]
        rpos = postorder[len(lin):-1]
        root = TreeNode(rval)
        root.left = self.buildTree(lin, lpos)
        root.right = self.buildTree(rin, rpos)
        return root
