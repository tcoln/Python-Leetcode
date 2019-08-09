# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        :note:
            递归的构造左右子树
        """
        if not nums:
            return None
        l = len(nums)
        root = TreeNode(nums[l/2])
        root.left = self.sortedArrayToBST(nums[:l/2])
        root.right = self.sortedArrayToBST(nums[l/2+1:])
        #print nums[:l/2], nums[l/2+1:]
        return root
