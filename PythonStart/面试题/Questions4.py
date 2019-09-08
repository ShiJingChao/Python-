"""
Question 1
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。

 

示例 1:

输入: 1
输出: "1"
示例 2:

输入: 4
输出: "1211"

"""
from itertools import groupby
# class Solution(object):
#     def countAndSay(self, n:int)->str:
#         """
#         :type n: int
#         :rtype: str
#         """
#         result = '1'
#         for i in range(1, n):
#             result = ''.join([str(len(list(g))) + k for k, g in groupby(result)])
#             print(result)
#             print("----",{k:str(len(list(g))) for k, g in groupby(result)})
#
#         return result
# s = Solution()
# print(s.countAndSay(5))

"""
Question 2

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
                1. dp问题. 公式为: dp[i] = max(nums[i], nums[i] + dp[i - 1])
                2. 最大子序和 = 当前元素自身最大, 或者 包含之前后最大
        """
        for i in range(1, len(nums)):
            # nums[i-1]代表dp[i - 1]
            nums[i] = max(nums[i], nums[i] + nums[i - 1])

        return max(nums)



        #
        # max_one = max(nums)
        # a = nums.index(max_one)
        # sum_all = 0
        # sum = a
        # for i in range(nums):
        #     sum_all += i
        # if sum_all < 0:
        #     return max_one
        # else:
        #     while True:
        #         if nums[a-1]+nums[a-2]>0:
        #             sum +=nums[a-1]+nums[a-2]





        # sum_nums = 0
        # one_max = max(nums)
        # m_max = min(nums)
        # if len(nums) == 1:
        #     return nums[0]
        # else:
        #     for i in nums:
        #         sum_nums += i
        #     for i in range(len(nums)):
        #         sum_p = nums[i]
        #         for j in range(i + 1, len(nums)):
        #             sum_p += nums[j]
        #             m_max = max(sum_nums, sum_p)
        #

        # return m_max

s = Solution()
print(s.maxSubArray([-2,1]))
# print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
# print(s.maxSubArray([3,-1,2,5]))


