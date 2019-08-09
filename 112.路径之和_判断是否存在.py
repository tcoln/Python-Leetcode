# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, suma):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        :note:
            深度遍历，记录当前路径和，直到叶子节点判断是否满足
        """
        if not root:
            return False
        
        def PreOrder(r, s):
            if not r:
                return False
            s += r.val
            print r.val, s
            if (not r.left) and (not r.right):
                if s == suma:
                    return True
                else:
                    return False                
            else:
                return PreOrder(r.left, s) or PreOrder(r.right, s) # 因为是or短路运算，左子树满足的时候右子树都没求解了，都不要剪枝了。
        
        return PreOrder(root, 0)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sums):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        def preorder(r, s):
            ans = False
            if not r.left and not r.right:
                if s + r.val == sums:
                    return True
            else:
                if r.left: ans = ans or preorder(r.left, s+r.val)
                if r.right: ans = ans or preorder(r.right, s+r.val)
            return ans
        
        return preorder(root, 0)        
