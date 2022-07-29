#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路: 分别获取左右子树的高度
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        return (
            abs(left - right) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )

    def get_height(self, root: TreeNode):
        if not root:
            return 0
        return max(self.get_height(root.left), self.get_height(root.right)) + 1


# @lc code=end
