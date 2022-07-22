#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 思路:递归构造左右子树,然后挂载到根节点
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        return self.build_tree(nums)

    def get_max_val_index(self, nums: List[int]):
        root = 0
        for i in range(len(nums)):
            if nums[i] > nums[root]:
                root = i
        return root

    def build_tree(self, nums: List[int]):
        max_val_index = self.get_max_val_index(nums)
        left = nums[:max_val_index]
        right = nums[max_val_index + 1 :]
        left_nodes, right_nodes = None, None
        if left:
            left_nodes = self.build_tree(left)
        if right:
            right_nodes = self.build_tree(right)
        root = TreeNode(val=nums[max_val_index], left=left_nodes, right=right_nodes)
        return root


# @lc code=end
