#三位水仙花数
#"水仙花数"是指一个三位整数，其各位数字的3次方和等于该数本身。
#请按照从小到大的顺序输出所有的3位水仙花数，请用"逗号"分隔输出结果。
s=""   #定义一个空列表，每当 for i in range(100,1000)循环找出一个水仙花数时，就会在s列表中加上一个水仙花数。最后输出的是一个水仙花数列表
for i in range(100,1000):
    t=str(i)
    if pow(eval(t[0]),3)+pow(eval(t[1]),3)+pow(eval(t[2]),3)==i:
        s+="{},".format(i)
print(s[:-1])   #输出的结果407后没有逗号，因为，在print(s[:-1])去掉了