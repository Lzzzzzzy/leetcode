#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路: 遍历整颗树,中序遍历得到整棵树的递增列表
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.val = []
        self.ret = True
        self.traverse(root)
        return self.ret

    def traverse(self, root):
        if not root:
            return
        self.traverse(root.left)
        pre = self.val[-1] if len(self.val) > 0 else -2147483649
        if pre >= root.val:
            self.ret = False
            return
        self.val.append(root.val)
        self.traverse(root.right)


# @lc code=end
