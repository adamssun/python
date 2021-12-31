#每天努力0.001或者不努力0.001的结果
dayfactor=0.004  #引入变量dayfactor，这样可以通过更改变量得到不同的结果
dayup=pow(1+dayfactor,365)
daydown=pow(1-dayfactor,365)
print('向上:{:.2f},向下:{:.2f}'.format(dayup,daydown))