#定义函数
from math import sqrt         #从math 库中引入平方根函数sqrt
def f(a,b):
    return sqrt (a**2+b**2)   #最后用return指明函数返回值
result=f(3,4)
print(result)
