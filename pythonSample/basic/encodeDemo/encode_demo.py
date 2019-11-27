# coding=utf-8
"""
    @author: asus
    @time: 2019/11/21
    @function: 测试编码格式
"""
import sys, locale


def write_str_default_encode():
    s = "我是一个str"
    print(s)
    print(type(s))
    print(sys.getdefaultencoding())
    print(locale.getdefaultlocale())

    with open("utf_file", "w", encoding="utf-8") as f:
        f.write(s)
    with open("gbk_file", "w", encoding="gbk") as f:
        f.write(s)
    with open("jis_file", "w", encoding="shift-jis") as f:
        f.write(s)


def str_transfor_bytes():
    s = '我是一个测试Str'
    print(type(s))
    # str 转bytes
    b = s.encode()
    print(b)
    print(type(b))
    # bytes转str
    c = b.decode()
    print(c)
    print(type(c))


if __name__ == '__main__':
    str_transfor_bytes()
