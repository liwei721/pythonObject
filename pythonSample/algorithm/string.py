# coding=utf-8
"""
~~~~~~~~~~~~~~~~~
 @Author：xuanke
 @contact: zhou.liwei@mydreamplus.com
 @date: 2019-10-29 16:13
 @function: 字符串处理相关的算法题
"""


def deleteSubStr():
    # 先输入两个字符串
    strA = input('strA: ')
    strB = input('strB: ')

    # 判断异常情况
    if strA is None or strA == '':
        return None
    if strB is None or strB == '':
        return strA

    # 将字符串转成list
    strAList = list(strA)
    strBList = list(strB)

    # 遍历寻找子串是否存在
    currentIndex = -1
    resultStr = ''
    for indexB in range(len(strBList)):
        for indexA in range(len(strAList)):
            if currentIndex > -1 and strAList[currentIndex + 1] == strBList[indexB]:
                currentIndex += 1
                break

            if strAList[indexA] == strBList[indexB]:
                currentIndex = indexA
                break

            # 如果不相等，就将字符串放到结果中
            resultStr += strAList[indexA]
    # 假如A没有遍历完，则拼接之后的字符串
    for indexC in range(currentIndex + 1, len(strAList)):
        resultStr += strAList[indexC]

    # 如果结果字符串和原输入字符串相等，则说明没子串
    if resultStr == strA:
        print('输入的子串B在子串A中不存在')
        return strA
    # 返回最终的结果
    return resultStr


if __name__ == '__main__':
    print(deleteSubStr())
