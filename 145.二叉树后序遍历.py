# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        :note:
            前序遍历是Pre：根、左、右，变形的前序遍历为Pre2：根、右、左，Pre2恰好是反序的Pos
            后
            序遍历是Pos：左、右、根
        """ 
        # Pre2的反序
        if not root:
            return []
        stack = [root]
        ans = []
        while len(stack) > 0:
            top = stack.pop()
            ans.append(top.val)
            if top.left:
                stack.append(top.left)
            if top.right:
                stack.append(top.right)
        ans.reverse()
        return ans
        
        # 递归
        def PostOreder(ro):
            if ro:
                ans = []
                l = PostOreder(ro.left)
                if l: 
                    ans.extend(l)
                r = PostOreder(ro.right)
                if r:
                    ans.extend(r)
                ans.append(ro.val)
                return ans
            return None
        return PostOreder(root)
        
