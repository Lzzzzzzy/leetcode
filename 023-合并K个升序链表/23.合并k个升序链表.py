#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思路: 回溯法
# 时间复杂度: 两链表合并的时间复杂度为O(m+n), m, n为两链表的长度.
# 多链表合并的复杂度则为k*O(m+n), k为链表个数
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        init_node = lists[0]
        for i in range(1, len(lists)):
            l = lists[i]
            if not l:
                continue
            init_node = self.mergeTwoLists(init_node, l)
        return init_node

    def mergeTwoLists(self, list1, list2):
        empty_header = ListNode()
        temp = empty_header
        while list1 and list2:
            if list1.val < list2.val:
                empty_header.next = list1
                list1 = list1.next
            else:
                empty_header.next = list2
                list2 = list2.next
            empty_header = empty_header.next
        empty_header.next = list2 if not list1 else list1
        return temp.next


# @lc code=end
