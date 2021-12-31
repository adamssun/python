'''天天向上的力量:工作日模式要努力到什么水平，才能与每天努力1%一样？
-A君: 一年365天，每天进步1%，不停歇 
-B君: 一年365天，每周工作5天休息2天，休息日下降1% ，要多努力呢？
每周工作5天休息2天，计算工作日的努力参数是多少才能与每天努力1%一样。'''
def dayup(df):
    dayup=1
    for i in range(365):      #计算思维
        if i%7 in [6,0]:
            dayup=dayup*(1-0.01)
        else:
            dayup=dayup*(1+df)
    return dayup
dayfactor=0.01
while dayup(dayfactor)<37.78:    #笨办法试错
    dayfactor+=0.001
print("工作日的努力参数是：{:.3f}".format(dayfactor))