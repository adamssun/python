import time
scale=50
print('执行开始'.center(scale//2,'-'))    #scall//2是设置这一行的宽度
start=time.perf_counter()
for i in range(scale+1):
    a='*'*i
    b='.'*(scale-i)
    c=(i/scale)*100
    dur=time.perf_counter()-start
    print('\r{:^3.0f}%[{}->{}]{:.2f}s'.format(c,a,b,dur),end='') 
    #  刷新的本质是：用后打印的字符覆盖之前的字符  
    #\r是在打印之前将光标停留在行首;end=空字符串，所以不会换行，会有光标停留效果;
    # 所以print这行代码的含义就是：打印一串字符串，打印之前将光标停在行首，打印之后不换行，将光标停留，然后要打印的时候光标还要停在行首......,这样就子能够形成了单行刷新效果
    #^指居中对齐，3指输出宽度为3；.0f指保留0位小数
    time.sleep(0.1)
    #循环每执行一次休眠0.1s
print('\n'+'执行结束'.center(scale//2,'-'))