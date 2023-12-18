#!/usr/bin/env python
def iscontain(A, B, accurate=False) -> bool:
    """
    It can check if A is a subset of B
    It supports both ordered and disordered modes
    Types such as list tuple strings are also supported
    基于python3.10，判断A是否是B的子集
    支持有序和无序两种模式，支持列表，元组，字符串等类型
    """
    if not accurate:
        dic1: dict = {}
        dic2: dict = {}
        for value1 in set(A):
            dic1[value1] = A.count(value1)
        for value2 in set(B):
            dic2[value2] = B.count(value2)
        for key in dic1:
            if key in dic2 and dic1[key] <= dic2[key]:
                continue
            else:
                return False
        else:
            return True
    else:
        num = 0
        for value2 in B:
            if value2 == A[num]:
                num += 1
                if num == len(A):
                    return True
            else:
                if num != 0:
                    num = 0
                else:
                    continue
        else:
            return False
