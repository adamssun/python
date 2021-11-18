score=eval(input('请输入成绩：'))
if score<60:
    print('不及格')
elif 60<=score<70:
    print('中')
elif 70<=score<90:
    print('良')
else:
    print("优")