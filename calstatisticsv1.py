def getnum():   #获取以逗号分隔的多个数据输入，输入为一行
    s=input()
    ls=list(eval(s))
    return ls
def mean(numbers):   #计算平均值
    s=0.0
    for num in numbers:
        s=s+num
    return s/len(numbers)
def dev(numbers,mean):   #计算标准差
    sdev=0.0
    for num in numbers:
        sdev=sdev+(num-mean)**2    #总体方差
    return pow(sdev/(len(numbers)-1),0.5)   
def median(numbers):    #计算中位数
    numbers.sort()
    size=len(numbers)
    if size%2==0:
        med=(numbers[size//2-1]+numbers[size//2])/2
    else:
        med=numbers[size//2]   #列表序号从0开始
    return med
n=getnum()
m=mean(n)
print('平均值:{:.2f},标准差:{:.2f},中位数:{}'.format(m,dev(n,m),median(n)))