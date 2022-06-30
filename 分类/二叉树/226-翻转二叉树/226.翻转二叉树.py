#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.traverse(root)
        return root

    def traverse(self, root):
        if not root:
            return
        self.traverse(root.left)
        self.traverse(root.right)
        tmp = root.left
        root.left = root.right
        root.right = tmp


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.right = left
        root.left = right
        return root


# @lc code=end
