def gettext():
    txt=open('hamlet.txt','r').read()
    txt=txt.lower()         #将所有单词变成小写
    for ch in '!"#$%^&*+-<?:;,/=>[\]_{|}~':
        txt=txt.replace(ch,'')   #将文本中特殊字符替换为空格
    return txt
hamlettxt=gettext()
words=hamlettxt.split()  #就是将一个字符串分隔成多个字符串组成的列表(重复 有序)
counts={}   #新建1个字典
for word in words:
    counts[word]=counts.get(word,0)+1   #一开始见到字典内的key的值，因为之前没有遇到过，所以就会给赋值后面的0；而对于第二轮的key，因为不是第一次见到了，所以不会赋给后面的值0,而是在他们key对应的value基础上+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)   #list.sort(key=None,reverse=False):key 是用来进行比较的元素，取自可迭代对象中的元素；reverse为排序规则；后面的x: x[1] 为对前面的对象中的第二维数据（即value）的值进行排序，x为items中的元素，x[1]为元素的字段索引。
for i in range(10):
    word,count=items[i]
    print(word)    #统计并输出出现最多的10个单词，每个单词一行