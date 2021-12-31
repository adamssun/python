import jieba
import wordcloud
from imageio import imread  #引用imread函数
mask=imread('fivestar.png')
f=open('新时代中国特色社会主义.txt','r',encoding='utf-8')
t=f.read()   #一次性读取全部内容
f.close()
ls=jieba.lcut(t)  #将文本分词形成列表
txt=' '.join(ls)   #将分词用空格分隔，形成长字符串
w=wordcloud.WordCloud(font_path='msyh.ttc',mask=mask,width=1000,height=700,background_color='white')    #以WordCloud对象为基础，配置参数、加载文本、输出文件；min_font_size指定词云中字体的最小字号，默认4号；max_font_size指定词云中字体的最大字号，根据高度自动调节；font_step指定词云中字体字号的步进间隔，默认为1；font_path指定字体文件的路径，默认None；max_words指定词云显示的最大单词数量，默认200；stop_words指定词云的排除词列表，即不显示的单词列表；mask指定词云形状，默认为长方形，需要引用imread()函数
w.generate(txt)   #向WordCloud对象w中加载文本txt
w.to_file('grwordcloud.png')   #将词云输出为图像文件，png或jpg格式