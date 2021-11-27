from random import random
from time import perf_counter
darts=1000*1000      #darts是1/4正方形内总共撒的随机点数量。
hits=0               #hits用于记录落在1/4圆形内的点的数量。
start=perf_counter()
for i in range(1,darts+1):
    x,y=random(),random()   #random()函数用于生成0~1之间的随机数，这里是一个单位圆，正好~如果不设置种子，会自动根据操作系统当前的时间（精确到毫秒）作为种子。因此，随机生成的1000*1000个点一定是各不相同的，不会发生点重叠的情况。
    dist=pow(x**2+y**2,0.5)
    if dist<=1.0:
        hits=hits+1
pi=4*(hits/darts)         #为了便于计算，我们先计算1/4圆的pi值，再乘以4，得到整个圆的pi值。
print('圆周率的值是:{:.9f}'.format(pi))
print('运行所用的时间是:{:.6f}s'.format(perf_counter()-start))