# iscontain
    基于python3.10，判断A是否为B子集
    It can check if A is a subset of B
    base on python 3.10
# usage
    支持有序与无序两种模式，支持列表，元组，字符串
    It supports both ordered and disordered modes
    Types such as list tuple strings are also supported
## disorder
```python
from iscontain import iscontain
l1 = [2, 4]
l2 = [2, 3, 4, 5, 4, 6]
print(iscontain(l1, l2))#True
```
## order
```python
from iscontain import iscontain
l1 = [2, 4]
l2 = [2, 3, 4, 5, 4, 6]
print(iscontain(l1, l2, accurate=True))#False
l1 = [4, 5, 4]
l2 = [2, 3, 4, 5, 4, 6]
print(iscontain(l1, l2, accurate=True))#True
```
