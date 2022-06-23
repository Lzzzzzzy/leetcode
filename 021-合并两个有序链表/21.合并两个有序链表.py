#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思路: 双指针分别遍历两个链表
# 时间复杂度: O(m+n), m,n为两个链表的长度
# runtime beats 41.81 %, memory usage beats 74.47 %
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 新链表
        ret = ListNode()
        # 虚拟头节点指针,不移动,永远指向头部
        init_node = ret
        while list1 and list2:
            if list1.val < list2.val:
                ret.next = list1
                list1 = list1.next
            else:
                ret.next = list2
                list2 = list2.next
            ret = ret.next
        # 如果有任意链表已经没有next节点了,则把另一个链表的剩余节点直接挂在新链表后面
        ret.next = list2 if not list1 else list1
        return init_node.next

# @lc code=end

