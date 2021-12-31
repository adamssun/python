tf=open('E:\\chrome\\fb.txt','rt')   #绝对路径，\为转义符，所以用\\表示\
print(tf.readline())
tf.close()

fo=open('E:\\chrome\\fb.txt','w+')
ls=['中国','法国','美国']
fo.writelines(ls)           #覆盖写
fo.seek(0)    #指针回到文件开头
for line in fo:
    print(line)
fo.close()

#一维数据的读入处理
#从特殊符号分离的文件中读入数据
f=open('f.txt').read()
ls=f.split('$')   #split用于根据分隔符将一个字符串进行拆分，返回一个列表
print(ls)


#一维数据的写入处理
#采用空格分隔方式将数据写入文件
ls=['中国','美国','日本']
f=open('f.txt','w')
f.write(' '.join(ls))   #join()函数是用于拼接字符串，即使用前面的‘ ’将后面的列表参数中元素拼接起来
f.close

#采用特殊分隔方式将数据写入文件
ls=['中国','美国','日本']
f=open('f.txt','w')
f.write('$'.join(ls))
f.close

#二维数据的读入处理
#二维数据一般索引习惯是ls[row][column]，先行后列
#从csv格式文件中读入数据。csv,comma-separated values，每行一个一维数据，采用逗号分隔，逗号与数据之间无额外空格，无空行；Excel和一般编辑软件都可以读入或另存为csv文件；如果某个元素缺失，逗号仍要保留；
fo=open('data.csv')
ls=[]
for line in fo:
    line=line.replace('\n','')  #去除每行的换行
    ls.append(line.split(','))  #将每行作为一个列表元素添加到列表中，每行中的元素用逗号分隔
fo.close()
print(ls)

#二维数据的写入处理
#将数据写入csv文件
ls=[[],[],[]]
fw=open('data.csv','w')
for item in ls:
    fw.write(','.join(item)+'\n')  #将ls中的列表元素覆盖写入文件，换行，每个列表元素中的元素用逗号分隔
fw.close()
print(ls)

#二维数据的逐一处理
#采用二层循环
ls=[[1,2],[3,4],[5,6]]
for row in ls:
    for column in row:
        print(column)
