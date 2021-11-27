from random import random,seed
DARTS=eval(input())   #撒点数
seed(123)             #随机数可以复现，确保每一次执行程序都会得到同样的结果即pi值是唯一的
hits=0.0              #撒中数
for i in range(DARTS):
    x,y=random(),random()
    dist=pow(x**2+y**2,0.5)   #距离圆心的距离
    if dist<=1.0:
        hits=hits+1
pi=4*(hits/DARTS)
print('{:.6f}'.format(pi))