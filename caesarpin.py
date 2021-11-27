#恺撒密码
#恺撒密码是古罗马恺撒大帝用来对军事情报进行加解密的算法，它采用了替换方法对信息中的每一个英文字符循环替换为字母表序列中该字符后面的第三个字符，即，字母表的对应关系下：       原文：A B C D E F G H I J K L M N O P Q R S T U V W X Z                        密文：D E F G H I J K L M N O P Q R S T U V W X Y Z A B C                      对于原文字符P，其密文字符C满足如下条件：C=(P+3) mod 26.  上述是凯撒密码的加密方法，解密方法反之，即：P=(C-3) mod 26.                                                 假设用户可能使用的输入包含大小写字母a~zA~Z、空格和特殊符号，请编写一个程序，对输入字符串进行恺撒密码加密，直接输出结果，其中空格不用进行加密处理。使用input()获得输入。     
s=input()
t=''      #起到不换行的作用，即每一次print输出都以t这个参数结尾
for c in s:
    if 'a'<=c<='z':
        t+=chr(ord('a')+((ord(c)-ord('a'))+3)%26) #ord(c)函数返回值为字符c的unicode编码，如ord('a')=97;chr(整数num)函数返回值为整数num（Unicode编码）对应的字符，如chr(97)='a'；为什么这样算？不清楚
    elif 'A'<=c<='Z':
        t+=chr(ord('A')+((ord(c)-ord('A'))+3)%26)
    else:
        t+=c
print(t)
