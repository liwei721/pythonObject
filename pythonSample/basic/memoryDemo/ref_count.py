# coding=utf-8
"""
~~~~~~~~~~~~~~~~~
 @Author：xuanke
 @contact: 784876810@qq.com
 @date: 2019-11-29 19:52
 @function: 验证引用计数增加和减少的场景
"""
import sys
import gc


def ref_method(str):
    print(sys.getrefcount(str))
    print("我调用了{}".format(str))
    print('方法执行完了')


def ref_count():
    # 引用计数增加的场景
    print('测试引用计数增加')
    a = 'ABC'
    print(sys.getrefcount(a))
    b = a
    print(sys.getrefcount(a))
    ref_method(a)
    print(sys.getrefcount(a))
    c = [1, a, 'abc']
    print(sys.getrefcount(a))

    # 引用计数减少的场景
    print('测试引用计数减少')
    del b
    print(sys.getrefcount(a))
    c.remove(a)
    print(sys.getrefcount(a))
    del c
    print(sys.getrefcount(a))
    a = 783
    print(sys.getrefcount(a))
    print(gc.get_referrers(a))


def threshold_gc():
    # 获取阈值
    print(gc.get_threshold())
    gc.set_threshold(800, 10, 10)
    print(gc.get_threshold())


def gc_method():
    # 启动垃圾回收
    gc.enable()
    # 停用垃圾回收
    gc.disable()
    # 指定垃圾回收的代数，不填写参数就是完全的垃圾回收
    gc.collect()
    # 设置垃圾回收的标志，多用于内存泄漏的检测
    gc.set_debug(gc.DEBUG_LEAK)
    # 返回一个对象的引用列表
    gc.get_referrers()


def cycle_method():
    a = []
    b = [a]
    a.append(b)

    del a
    del b
    print('end')



if __name__ == '__main__':
    cycle_method()
