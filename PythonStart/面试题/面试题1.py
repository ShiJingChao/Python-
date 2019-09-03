"""
转换为七进制

"""

# def convertToBase7(num):
#     """
#     :type num: int
#     :rtype: str
#     """
#     b = ""
#     while True:
#         s = num // 7
#         y = num % 7
#         b = b + str(y)
#         if s == 0:
#             break
#         num = s
#     v = b[::-1]
#     print(v)
# convertToBase7(100)

"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
"""

# class Solution(object):
# #     def isAnagram(self, s, t):
# #         """
# #         :type s: str
# #         :type t: str
# #         :rtype: bool
# #         """
# #         for i in s:
# #             if i in t and len(s) == len(t):
# #                 return True
# #             else:
# #                 return False




"""

给定的整数数组 A ，我们要将 A数组 中的每个元素移动到 B数组 或者 C数组中。（B数组和C数组在开始的时候都为空）

返回true ，当且仅当在我们的完成这样的移动后，可使得B数组的平均值和C数组的平均值相等，并且B数组和C数组都不为空。

示例:
输入: 
[1,2,3,4,5,6,7,8]
输出: true
解释: 我们可以将数组分割为 [1,4,5,8] 和 [2,3,6,7], 他们的平均值都是4.5。
注意:

A 数组的长度范围为 [1, 30].
A[i] 的数据范围为 [0, 10000].
"""
A = [1,2,3,4,5,6,7,8]
B = []
C = []




"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""
class Solution:
    def twoSum(self, nums, target):
        """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
        """
        hashmap = {}    # 定义一个字典
        for index, num in enumerate(nums):  #
            print(index,num)
            another_num = target - num
            if another_num in hashmap:
                print(hashmap[another_num],index)
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None


p = Solution()
print(p.twoSum([2,5,5,11], 10))



"""


"""


# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         if x < 0:
#             abs(x)
#             x = str(x)
#             x = x[::-1]
#             if x[0] == 0:
#                 print("-"+x[::])
#             else:
#                 print("-"+x)
#         else:
#             x = str(x)
#             x = x[::-1]
#             if x[0] == 0:
#                 print("-"+x[::])
#             else:
#                 print("-"+x)
#
#
# p = Solution()
# p.reverse(100)


