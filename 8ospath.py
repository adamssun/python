#路径操作
import os.path as op
op.abspath('hamlet.txt')  #返回文件在当前系统中的绝对路径

op.normpath('C://Users//Administrator//Code//python//hamlet.txt')   #归一化path的表示方式，统一用\\分隔路径；结果为'C:\\Users\\Administrator\\Code\\python\\hamlet.txt'

op.relpath('C://Users//Administrator//Code//python//hamlet.txt')   #返回当前程序于文件之间的相对路径

op.dirname("D://PYE//file.txt")   #返回path中的目录名称

op.basename('D://PYE//file.txt')  #返回path中最后的文件名称

op.join('D://','PYE//file.txt')   #组合两个参数，返回一个路径字符串
