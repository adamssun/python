#《沉默的羔羊》之最多单词
#附件是《沉默的羔羊》中文版内容，请读入内容，分词后输出长度大于等于2且出现频率最多的单词。
#如果存在多个单词出现频率一致，请输出按照Unicode排序后最大的单词。
import jieba
f=open('沉默的羔羊.txt',encoding='utf-8')
ls=jieba.lcut(f.read())
d={}
for w in ls:
    if len(w)>=2:
        d[w]=d.get(w,0)+1
maxc=0     #次数count
maxw=''    #单词word
for k in d:
    if d[k]>maxc:
        maxc=d[k]
        maxw=k
    elif d[k]==maxc and k>maxw:
        maxw=k
print(maxw)
f.close()