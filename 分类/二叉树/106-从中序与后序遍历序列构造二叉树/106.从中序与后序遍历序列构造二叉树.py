#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 思路: 同105,根据后续遍历的结果找根节点,中序遍历的结果分别找到左子树和右子树的值,再build
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return
        root_val = postorder[-1]
        left_size = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = self.buildTree(inorder[:left_size], postorder[:left_size])
        root.right = self.buildTree(inorder[left_size + 1 :], postorder[left_size:-1])
        return root


# @lc code=end
