from types import MemberDescriptorType


def getnum():   #获取用户不定长度的输入
    nums=[]
    inumstr=input('请输入数字（回车退出）：')
    while inumstr!='':
        nums.append(eval(inumstr))   #将数值添加到列表中
        inumstr=input('请输入数字（回车退出）：')
    return nums
def mean(numbers):   #计算平均值
    s=0.0
    for num in numbers:
        s=s+num 
    return s/len(numbers)   #len()用于获取列表中元素的数量
def dev(numbers,mean):    #计算方差deviation
    sdev=0.0              #standard deviation
    for num in numbers:
        sdev=sdev+(num-mean)**2
    return pow(sdev/(len(numbers)-1),0.5)
def median(numbers):      #计算中位数
    sorted(numbers)       #将列表排序
    size=len(numbers)
    if size%2==0:
        med=(numbers[size//2-1]+numbers[size//2])/2
    else:
        med=numbers[size//2]
    return med 
n=getnum()
m=mean(n)
print('平均值：{},方差：{:.2},中位数：{}'.format(m,dev(n,m),median(n)))


