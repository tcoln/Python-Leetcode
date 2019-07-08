tion for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        :note:
            方法一：中序遍历即可，时间是O(n)
            方法二: 分别统计左右子树的最左、最右高度，若相等则为满二叉树，节点数=2^h-1；否则递归调用左右子树，时间复杂度O(h^2)
        """
        
        def InOrder(root):
            count = 0
            if root != None:
                count += 1
                count += InOrder(root.left)
                count += InOrder(root.right)
            return count
        
        def TreeHeight(root, leftOrRight):
            h = 0
            tmp = root
            while(tmp):
                h += 1
                if leftOrRight == 0:
                    tmp = tmp.left
                else:
                    tmp = tmp.right
            return h
        
        def myCountNodes(root):
            count = 0
            if root != None:
                lh = TreeHeight(root, 0)
                rh = TreeHeight(root, 1)
                if lh == rh:
                    count = pow(2,lh) - 1
                else:
                    count = myCountNodes(root.left) + myCountNodes(root.right) + 1
            return count
                
        # solution 1
        count = InOrder(root)
        
        # solution 2
        count = myCountNodes(root)
            
        return count
