#获取标准文本
def gettext():
    txt=open('hamlet.txt','r').read()
    txt=txt.lower()
    for ch in '~!@#$%^&*()_+":<>?=-,/[]{}\|':
        txt=txt.replace(ch,'')
    return txt

#创建字典counts
hamlettxt=gettext()
words=hamlettxt.split()  #创建一个列表
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1

#将字典转化成列表进行排序
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)  #默认排序是从小到大，将reverse=true是将排序设为从大到小
for i in range(10):
    word,count=items[i]
    print('{0:<10}{1:>5}'.format(word,count))
