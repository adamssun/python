#有三个圆柱A、B、C，初始时A上有N个圆盘，N由用户输入给出，最终移动到圆柱C上。
#每次移动步骤的表达方式示例如下：[STEP 10] A->C。其中，STEP是步骤序号，宽度为4个字符，右对齐
steps=0
def hanoi(src,des,mid,n):   #通过中间柱子将源柱子上的N个圆盘移动到目标柱子上
    global steps          
    if n==1:              #基例
        steps+=1
        print('[STEP{:>4}]{}->{}'.format(steps,src,des))
    else:                 #递归链条
        hanoi(src,mid,des,n-1)   #先通过目标柱子将源柱子上的n-1个圆盘移动到中间柱子上
        steps+=1
        print('[STEP{:>4}]{}->{}'.format(steps,src,des))  #将剩余的最下面一个圆盘即第n个圆盘移动到目标柱子
        hanoi(mid,des,src,n-1)   #再调用函数将在中间柱子上的n-1个圆盘通过源柱子移动到目标柱子上，从容实现递归
N=eval(input())  #获取用户输入的圆盘数
hanoi('A','C','B',N)   #调用函数执行程序将A柱子上的N个圆盘移动到C柱子
print(steps)