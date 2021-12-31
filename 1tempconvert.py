#温度转换
#转换公式：C=(F-32)/1.8
Tempstr=input("请输入带有符号的温度值：")   #input()是输入函数，用户输入的信息以字符串类型保存在变量中
if Tempstr[-1] in ['F','f']:      #Tempstr[-1],通过索引返回字符串中单个字符
    C=(eval(Tempstr[0:-1])-32)/1.8   #Tempstr[0:-1],通过切片返回字符串中一段字符子串
    print ('转换后的温度是{:.2f}C'.format(C))   #print()是输出函数，以字符形式向控制台输出结果的函数，引号仅在程序内部使用，输出无引号；{}表示槽，{:.2f}表示将变量C填充到这个位置时取小数点后2位
elif Tempstr[-1] in ['C','c']:
    F=1.8*(eval(Tempstr[0:-1]))+32   #eval()函数用于去除参数最外侧引号并执行余下语句。eval('print("hello")')的返回值为hello
    print ('{:.2f}F'.format(F))
else:
    print ('输入格式错误')