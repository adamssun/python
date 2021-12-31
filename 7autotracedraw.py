import turtle as t
t.title('自动轨迹绘制')    #窗口的标题
t.setup(800,600,0,0)
t.pencolor('red')
t.pensize(5)
#数据读取
datals=[]
f=open('data.txt')
for line in f:
    line=line.replace("\n","")    #将每一行末尾的换行替换成空字符串
    if line !='':                 #eval函数不能用于空行，而txt文件末尾可能有很多空行，所以进行排除
        datals.append(list(map(eval,line.split(","))))    #line.split()是将每一行的字符用“，”分隔；内嵌函数map()是将第一个函数参数应用于第二个参数中的每一个元素；eval()能够将一个字符串两侧的引号去掉；datals列表的每一个元素是每一行经过处理后形成的小列表
                 #疑问：line.split()返回的就是一个列表，为何还需要前面加个list?   因为map() doesn't return a list, it returns a map object.You need to call list(map) if you want it to be a list again.
f.close()
#自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])   #每一个i元素都是一个小列表，列表中是自定义的一串数据接口，如【300,0,144,1,0,0】，我们定义300为行进距离；0为转向判断，0是向左转，1是向右转；144是转向角度，后三位是RGB三个通道颜色，0-1之间的浮点数；data[i][3]是将i元素列表中的第3位的值赋给pencolor
    t.fd(datals[i][0])  #将第0位行进距离赋值给fd
    if datals[i][1]:     #判断第1位是1还是0
        t.right(datals[i][2])   #将第2位转向角度赋值给right
    else:
        t.left(datals[i][2])
