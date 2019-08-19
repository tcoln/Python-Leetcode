# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        :note:
            先一直往左走到头，然后弹栈输出，再继续压右节点
        """
        if not root: return []
        ret, stack = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                cur = stack.pop()
                ret.append(cur.val)
                root = cur.right
        return ret
