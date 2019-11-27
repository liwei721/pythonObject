"""
    @author: asus
    @time: 2019/11/27
    @function: 测试python内存
"""
import sys


def ref_count_test():
    str1 = 'ABC'
    str2 = str1
    print(sys.getrefcount(str1))
    print(sys.getrefcount(str2))


if __name__ == '__main__':
    ref_count_test()
