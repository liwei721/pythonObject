# coding=utf-8
"""
    @author: xuanke
    @time: 2019/11/27
    @function: 测试python内存
"""
import sys


class RefClass(object):
    def __init__(self):
        print("this is init")


def ref_count_test():
    # 验证普通字符串
    str1 = "abc"
    print(sys.getrefcount(str1))
    # 验证稍微复杂点的字符串
    print(sys.getrefcount("xuankeTester"))
    # 验证小的数字
    print(sys.getrefcount(12))
    # 验证大的数字
    print(sys.getrefcount(257))
    print(sys.getrefcount(257))
    # 验证类
    a = RefClass()
    print(sys.getrefcount(a))
    # 验证引用计数增加
    b = a
    print(sys.getrefcount(a))

    # 验证引用计数减少
    b = None
    print(sys.getrefcount(a))


def memory_address_test():
    str1 = 'xuankeTester'
    str2 = 'xuankeTester'
    print(id(str1))
    print(id(str2))

    str3 = 'abc'
    str4 = 'abc'
    print(id(str3))
    print(id(str4))

    a = 12
    b = 12
    print(id(a))
    print(id(b))

    c = 257
    d = 257
    print(id(c))
    print(id(d))

if __name__ == '__main__':
    memory_address_test()
