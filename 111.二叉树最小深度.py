# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        :note:
            递归地返回左右子树中的最小深度+1，注意最小深度是叶子节点路径，一边子树为空的情况
            从最简单的考虑清楚，空树、左子树空、右子树空、左右子树都为空
        """
        if not root:
            return 0
        def getMinH(r):
            if not r:
                return 0
            if not r.left:
                return getMinH(r.right) + 1
            if not r.right:
                return getMinH(r.left) + 1
            return min(getMinH(r.left), getMinH(r.right)) + 1
        return getMinH(root)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right))+1
        
