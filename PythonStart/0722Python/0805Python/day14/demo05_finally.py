"""
    finally 和 else

    try:
        代码
    except:
        pass
    except Exception :
        处理
    else:
        没有发生异常时, 执行的代码块
    finally:
        无论有没有发生异常, 都会执行
"""

# try:
#     num = input("请输入一个整数:")
#     num = int(num)
#     num = 6 / num
# except:    # 不关心是什么类型的异常, 也不需要拿到异常的对象, 只要是异常, 我就统一一个处理方式, 则....
#     print("-------发生了异常, 我来处理一下--------")
# else:
#     print("没有发生异常, 所以最终num计算的结果是:", num)
# finally:
#     print("无论有没有异常, 都会执行-------over--------")
#
#
#
#
# def add(a,b):
# #     return a + b
# # def test():
# #     for r_i in range(4):
# #         yield r_i  #0,1,2,3
# # g = test()
# # for n in [2,10]:  #2,10
# #     g = (add(n,i) for i in g)
# # print(list(g))
# def findDisappearedNumbers(nums):
#     for n in nums:
#         nums[abs(n) - 1] = -abs(nums[abs(n) - 1])
#     return [i + 1 for i, n in enumerate(nums) if n > 0]
#
# a = findDisappearedNumbers([4,3,-2,7,8,2,3,1])
# print(a)

