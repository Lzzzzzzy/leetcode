#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路1: 遍历整颗树
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ret = []
        self.traverse(root)
        return self.ret

    def traverse(self, root):
        if not root:
            return []
        self.traverse(root.left)
        self.ret.append(root.val)
        self.traverse(root.right)


# 思路2:分解子树
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        if not root:
            return []
        left = self.inorderTraversal(root.left)
        ret.extend(left)
        ret.append(root.val)
        right = self.inorderTraversal(root.right)
        ret.extend(right)
        return ret


# @lc code=end
