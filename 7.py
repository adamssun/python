#文件字符分布
#统计附件文件的小写字母a-z的字符分布，即出现a-z字符的数量，并输出结果
#同时请输出文件一共包含的字符数量
#注意输出格式，各元素之间用英文逗号（,）分隔。
#答案可能包含a-z共26个字符的分布，如果某个字符没有出现，则不显示，输出顺序a-z顺序

fo=open('latex.log')
cc=0
d={}
for i in range(26):
    d[chr(ord('a')+i)]=0   #将a-z的初始数量设为0，但经验证，没有这一步也可以
for line in fo:
    for c in line:
        d[c]=d.get(c,0)+1    ##d.get(k,default) 键k存在返回相应值，不在则返回default
        cc+=1
print('共{}字符'.format(cc),end='')    #不换行
for i in range(26):         #使用 ord('a')+i 配合 range()函数 可以遍历一个连续的字符表 
    if d[chr(ord('a')+i)]!=0:    #字符未出现则不统计     
        print(',{}:{}'.format(chr(ord('a')+i),d[chr(ord('a')+i)]),end='')


#文件独特行数
#统计附件文件中与其他任何其他行都不同的行的数量，即独特行的数量

f=open('latex.log')
ls=f.readlines()
s=set(ls)
for i in s:
    ls.remove(i)    #ls.remove()可以去掉某一个元素，如果该行是独特行，去掉该元素后将不在集合t中出现
t=set(ls)
print('共{}独特行'.format(len(s)-len(t)))



#文本的平均列数
#打印输出附件文件的平均列数，计算方法如下：
#（1）有效行指包含至少一个字符的行，不计算空行；
#（2）每行的列数为其有效字符数
#（3）平均列数为有效行的列数平均值，采用四舍五入方式取整数进位
f=open('latex.log','r')
s=0
c=0
for line in f.readlines():
    line=line.strip('\n')
    if line=='':
        continue
    s+=len(line)
    c+=1
avg=round(s/c)
avg=int(avg)
print(avg)

#CSV格式清洗与转换
f=open('data1.csv')
ls=f.readlines()    #读入文件所有行，以每行为元素形成列表
ls=ls[::-1]         #将整个列表倒序
lt=[]
for item in ls:      #将每行中的元素倒序
    item=item.strip('\n')       
    item=item.replace(' ','')   #去除每行的前后空格
    lt=item.split(',')       #以列表的形式返回用，分隔的字符串
    lt=lt[::-1]
    print(';'.join(lt))        #用；分隔lt中的元素
f.close