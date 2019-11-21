"""
    @author: asus
    @time: 2019/11/21
    @function: 验证编码格式
"""
import sys, locale


def test_case1():
    s = "小甲"
    print(s)
    print(type(s))
    print(sys.getdefaultencoding())
    print(locale.getdefaultlocale())

    with open("utf1", "w", encoding="utf-8") as f:
        f.write(s)
    with open("gbk1", "w", encoding="gbk") as f:
        f.write(s)
    with open("jis1", "w", encoding="shift-jis") as f:
        f.write(s)

if __name__ == '__main__':
    test_case1()