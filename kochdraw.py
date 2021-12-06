import turtle as t
def koch(size,n):   #1阶科赫曲线就是将一条size的线段分成三段，去掉中间的一段，然后让中间绘制一个凸起的三角形
    if n==0:
        t.fd(size)
    else:
        for angle in [0,60,-120,60]:   #假设n==1，则相当于执行了四次koch(size/3,0),即第一步前进size/3，第二步左转60度前进size/3，第三步左转-120度前进size/3，第四步左转60度前进size/3；n阶就是在角度为0的时候绘制一个尺寸是当前三分之一的科赫曲线，然后左转60度绘制一个尺寸是当前三分之一的科赫曲线，然后左转-120度绘制一个尺寸是当前三分之一的科赫曲线，最后左转60度绘制一个尺寸是当前三分之一的科赫曲线
            t.left(angle)
            koch(size/3,n-1)
def main(level):
    t.setup(600,600)
    t.penup()
    t.goto(-200,100)
    t.pendown()
    t.pensize(2)
    koch(400,level)    #绘制首尾相连的三段科赫曲线，形成科赫雪花，如果不绘制科赫曲线，会是一个三角形
    t.right(120)
    koch(400,level)
    t.right(120)
    koch(400,level)
    t.hideturtle()
try:
    level=eval(input('请输入科赫曲线的阶：'))
    main(level)
except:
    print('输入错误')