#获取星期字符串
weekstr='星期一星期二星期三星期四星期五星期六星期日'
weekid=eval(input('请输入星期数字（1-7）：'))
pos=(weekid-1)*3     
print(weekstr[pos:pos+3])   #通过切片返还相应的字符串，如用户输入为2，则返还索引为【3：6】的字符串，即星期二

weekstr1='一二三四五六七'
weekid1=eval(input('请输入星期数字（1-7）：'))
print('星期'+weekstr1[weekid1-1])