"""
Questions 1
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

示例 1:

输入: "III"
输出: 3
示例 2:

输入: "IV"
输出: 4
示例 3:

输入: "IX"
输出: 9
示例 4:

输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
示例 5:

输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.


"""

#
# class Solution(object):
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         sum = 0
#         dict1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#         if len(s) == 1:
#             return dict1[s]
#         for i in range(-1,-len(s),-1):
#             if dict1[s[i - 1]] < dict1[s[i]] and i == -1:
#                 sum = dict1[s[i]] - dict1[s[i-1]]
#
#             elif dict1[s[i-1]] >= dict1[s[i]] and i == -1:
#                 sum = dict1[s[i]] + dict1[s[i-1]]
#             elif dict1[s[i-1]] < dict1[s[i]]:
#                 sum -= dict1[s[i-1]]
#             elif dict1[s[i-1]] >= dict1[s[i]]:
#                 sum += dict1[s[i-1]]
#         return sum
#
# p = Solution()
# print(p.romanToInt("MCMXCIV"))




"""
Questions 2

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。



"""

# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         strs = sorted(strs,key =len)




# s = Solution()
# print(s.longestCommonPrefix(["abc","ac","defg","abcer"]))


"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool

        """
        
        # a = len(s)
        # l = []
        # for i in range(a):
        #     l.append(0)
        # for i in range(a):
        #     if i == 0:
        #         l[0] = s[0]
        #     else:
        #         j = i - 1
        #         while l[j] == 0:
        #             j -= 1
        #             if j == -1:
        #                 break
        #         if j == -1 or s[i] == '(' or s[i] == '[' or s[i] == '{':
        #             l[i] = s[i]
        #         elif l[j] == "(" and s[i] == ')' or l[j] == '[' and s[i] == ']' or l[j] == '{' and s[i] == '}':
        #             l[j] = 0
        #         else:
        #             return False
        # else:
        #     if a == 0:
        #         return True
        #     for i in l:
        #         if i != 0:
        #             return False
        #     else:
        #         return True


# s = Solution()
# print(s.isValid("({}[()][()])"))

