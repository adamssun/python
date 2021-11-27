#读入一个字典类型的字符串，反转其中键值对输出。即，读入字典key:value模式，输出value:key模式。
s=input()   
try:
    d=eval(s)
    e={}
    for k in d:
        e[d[k]]=k
    print(e)
except:
    print('输入错误')    #用户输入的字典格式的字符串，如果输入不正确，提示：输入错误。