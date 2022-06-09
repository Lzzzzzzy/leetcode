#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
import math
from typing import List

# @lc code=start

# 思路1: 中位数: 是按顺序排列的一组数据中居于中间位置的数
# 分为奇数和偶数两种情况.如果两个list相加的长度为奇数,则中位数为合并后数组的中间位置的数;偶数情况为中间两个位置的数相加除2
# 题目中说两个数组都是有序的,所以两个数组左边都创建一个指针,对比指针指向的数字的结果,哪边小就放到新合并的数组中,指针右移一位.
# 奇数: 如果合并的数组长度 > 两数组长度和的一半,则中位数为合并数组的最后一个元素
# 偶数: 如果合并的数组长度 > 两数组长度和的一半 + 1, 则中位数为合并数组的最后两个元素之和/2
# 时间复杂度: O(m+n) 空间复杂度: 最大为O(m+n)
# runtime: beats 8.56%, memory usage beats 48.21%

# 可优化的点: 不用创建新数组,直接取指针指向的值即可


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_sum = len(nums1) + len(nums2)
        # 创建一个新数组,用来保存合并后的结果
        nums3 = []
        # 两个指针分别指向两个数组左端
        i, j = 0, 0
        # 遍历两个数组,将结果加到新的合并数组中
        while len(nums3) <= len_sum / 2:
            while i < len(nums1):
                # 如果新数组长度够了,则退出循环
                if len(nums3) > len_sum / 2:
                    break
                # 如果j已经指到了nums2的末尾,即nums2的所有元素都放到了新数组中,则一直把nums1的元素加到新数组末尾即可
                if j >= len(nums2) or nums1[i] <= nums2[j]:
                    nums3.append(nums1[i])
                    i += 1
                else:
                    break
            while j < len(nums2):
                # 如果新数组长度够了,则退出循环
                if len(nums3) > len_sum / 2:
                    break
                # 如果i已经指到了nums1的末尾,即nums1的所有元素都放到了新数组中,则一直把nums2的元素加到新数组末尾即可
                if i >= len(nums1) or nums2[j] < nums1[i]:
                    nums3.append(nums2[j])
                    j += 1
                else:
                    break
        # 数组长度总和为奇数
        if len_sum % 2 == 1:
            return nums3[-1]
        # 数组长度总和为偶数
        return (nums3[-1] + nums3[-2]) / 2


# 思路2: 看到数组有序,自然而然想到二分法.思路1的算法相当于每次排除一个元素,二分法则每次排除多个元素
# 找中位数相当于找第k小的数.奇数情况下,k=数组长度之和/2 向上取整;偶数情况下,k1=数组长度之和/2, k2=数组长度之和/2+1.
# 两种情况合并一下,会发现偶数其实也只需要找到k即可
# 单数组的情况下, 例如[1,2,3,4,5], 找第3小的数,就是看指针指向的位置到数组起始之间的位置是否跨越了2个元素
# 多数组的情况下, 则可以将 K/数组个数, 向下取整, 用每次排除的元素个数来变更K的值
# runtime: beats 65.4%, memory usage beats 63.71%
class Solution:
    def getKth(self, nums1: List[int], nums2: List[int], k: int) -> float:
        # 保证nums1是最短的数组,可以消除一些多余判断
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # 当Nums1为空时,直接取nums2的第k-1个元素
        if not nums1:
            return nums2[k - 1]

        # 当k=1时,返回两个列表中第0个元素的值即可
        if k == 1:
            return min(nums1[0], nums2[0])

        # 二分法,i和j考虑边界情况
        half_k = math.floor(k / 2)
        i, j = min(half_k, len(nums1)) - 1, min(half_k, len(nums2)) - 1

        # 每次排除的元素都直接截掉,用新数组找k,k做相应变化
        # todo: 此处可优化,不新生成数组,降低空间复杂度
        if nums1[i] > nums2[j]:
            k -= j + 1
            nums2 = [] if j == len(nums2) else nums2[j + 1 :]
        else:
            k -= i + 1
            nums1 = [] if i == len(nums1) else nums1[i + 1 :]
        # 递归
        return self.getKth(nums1, nums2, k)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_sum = len(nums1) + len(nums2)
        k = math.ceil(len_sum / 2)

        # 奇数时取第K个数
        if len_sum % 2 == 1:
            return self.getKth(nums1, nums2, k)
        # 偶数时取第K个和K+1个数,两数之和/2
        num1 = self.getKth(nums1, nums2, k)
        num2 = self.getKth(nums1, nums2, k + 1)
        return (num1 + num2) / 2


# @lc code=end
