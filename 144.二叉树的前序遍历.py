# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        :note:
            当栈不为空的时候，弹出栈顶元素，然后分布入栈右左子节点
        """
        if not root:
            return []
        stack = [root]
        ans = []
        while len(stack) > 0:
            top = stack.pop()
            ans.append(top.val)
            if top.right:
                stack.append(top.right)
            if top.left:
                stack.append(top.left)
        return ans
        
