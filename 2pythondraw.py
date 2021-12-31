import turtle as t
t.setup(650,350,200,200)  #设置绘图窗体，650为窗体长度，350为窗体宽度，第一个200为距离屏幕左侧距离，第二个200为距离屏幕上侧距离，后两个参数默认值为窗体居中
t.penup()
t.fd(-250)   #不改变方向，倒退行进
t.pendown()
t.pensize(25)
t.pencolor('purple')
t.seth(-40)    #设置海龟的绝对角度
for i in range(4):
    t.circle(40,80)   #以海龟左侧40像素的点为圆心，画80度的弧
    t.circle(-40,80)
t.circle(40,80/2)
t.fd(40)
t.circle(16,180)
t.fd(40*2/3)
t.done()
