from random import random,seed
DARTS=eval(input())   #撒点数
seed(123)             #seed(a=None):初始化给定的随机数种子，默认为当前系统时间；随机数可以复现，确保每一次执行程序都会得到同样的结果即pi值是唯一的。seed(123)产生种子10对应的序列
hits=0.0              #撒中数
for i in range(DARTS):
    x,y=random(),random()   #random()生成一个【0.0,1.0】之间的随机小数
    dist=pow(x**2+y**2,0.5)   #距离圆心的距离
    if dist<=1.0:
        hits=hits+1
pi=4*(hits/DARTS)
print('{:.6f}'.format(pi))