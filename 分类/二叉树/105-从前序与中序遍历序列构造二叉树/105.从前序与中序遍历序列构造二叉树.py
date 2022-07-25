#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路: 前序遍历的第一个节点就是根节点,通过根节点和中序遍历的结果找到左右子树的结果,分别递归构造左右子树
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return
        root_val = preorder[0]
        root = TreeNode(root_val)
        left_size = inorder.index(root_val)
        root.left = self.buildTree(preorder[1 : left_size + 1], inorder[:left_size])
        root.right = self.buildTree(preorder[left_size + 1 :], inorder[left_size + 1 :])
        return root


# @lc code=end
