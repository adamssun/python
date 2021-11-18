height,weight=eval(input('请输入您的身高（米）和体重（公斤）【逗号分隔】：'))
bmi=weight/pow(height,2)
print('你的bmi值是：{:.2f}'.format(bmi))
who,nat='',''     #注意多变量同时赋值的方法，中间使用逗号分隔
if bmi<18.5:
    who,nat='偏瘦','偏瘦'
elif 18.5<=bmi<24:
    who,nat='正常','正常'
elif 24<=bmi<25:
    who,nat='正常','偏胖'
elif 25<=bmi<28:
    who,nat='偏胖','偏胖'
elif 28<=bmi<30:
    who,nat='偏胖','肥胖'
else:
    who,nat='肥胖','肥胖'
print('bmi国际指标：{0},国内指标：{1}'.format(who,nat))   #.format()方法使用时，{}槽可以指定第几位