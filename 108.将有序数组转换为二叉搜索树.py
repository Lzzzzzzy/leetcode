#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路: 要使左右子树高度相差不超过1,则根节点需要在数组的中间
# 找到根节点后确定左右子树的值,再递归构造左右子树
# runtime beats 91.08 %, memory usage beats 65.51 %
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return
        root_val_idx = len(nums) // 2
        root_val = nums[root_val_idx]
        root = TreeNode(root_val)
        root.left = self.sortedArrayToBST(nums[:root_val_idx])
        root.right = self.sortedArrayToBST(nums[root_val_idx + 1 :])
        return root


# @lc code=end
