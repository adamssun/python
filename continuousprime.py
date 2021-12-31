#连续质数计算
#获得用户输入数字N，计算并输出从N开始的5个质数，单行输出，质数间用逗号,分割。
#注意：需要考虑用户输入的数字N可能是浮点数，应对输入取整数；最后一个输出后不用逗号。
def prime(m):
    for i in range(2,m):
        if m%i==0:
            return False
    return True

n=eval(input())   #求取字符串的值
n_=int(n)         #将求取的值转为整数
n_=n_+1 if n_<n else n_   #如果输入的是浮点数，则取整后要+1
count=5

while count>0:
    if prime(n_):
        if count>1:
            print(n_,end=',')
        else:
            print(n_,end='')   #输出最后一位质数时不带逗号
        count-=1
    n_+=1
        