# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, suma):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        :note:
            深度遍历，记录当前路径，直到叶子节点判断是否满足
            上一题先序遍历有返回值，这一题没有返回值
        """
        if not root:
            return []
        ans = []
        def PreOrder(r, path):
            if not r:
                return
            newP = list(path)
            newP.append(r.val)
            if (not r.left) and (not r.right):
                if sum(newP) == suma:
                    ans.append(newP)             
            else:
                PreOrder(r.left, newP)
                PreOrder(r.right, newP)
        
        PreOrder(root, [])
        return ans
        
