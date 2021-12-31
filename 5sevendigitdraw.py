import turtle as t
import time
def drawgap():     #绘制数码管间隔
    t.penup()
    t.fd(5)
def drawline(draw):    #绘制单段数码管
    drawgap()
    t.pendown() if draw else t.penup()
    t.fd(40)
    drawgap()
    t.right(90)
def drawdigit(d):     #根据数字绘制单个数字的七段数码管
    drawline(True) if d in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if d in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if d in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if d in [0,2,6,8] else drawline(False)
    t.left(90)
    drawline(True) if d in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if d in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if d in [0,1,2,3,7,8,9] else drawline(False)
    t.left(180)
    t.penup()
    t.fd(20)
def drawdate(date):   #date为日期，格式为'%Y-%m=%d+'
    t.pencolor('red')
    for i in date:
        if i=='-':
            t.write('年',font=('Arial',18,'normal'))   #将-替换成年
            t.pencolor('green')
            t.fd(40)
        elif i=='=':
            t.write('月',font=('Arial',18,'normal'))   #将=替换成月
            t.pencolor('blue')
            t.fd(40)
        elif i=='+':                              
            t.write('日',font=('Arial',18,'normal'))    #将+替换成日
        else:
            drawdigit(eval(i))
def main():
    t.setup(800,350,200,200)   #画布尺寸，长，宽，左顶点距离左边屏幕和上面屏幕的距离
    t.penup()
    t.fd(-300)  #倒退300补，不改变方向
    t.pensize(5)
    drawdate(time.strftime('%Y-%m=%d+',time.gmtime()))  #%y 两位数的年份表示（00-99），%Y 四位数的年份表示（000-9999）%m 月份（01-12），%d 月内中的一天（0-31）；strftime是将获取的时间转换为字符串，gmtime()是获取系统时间
    t.done()
main()
