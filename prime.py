#求100以内所有素数之和并输出。
#素数指从大于1，且仅能被1和自己整除的整数。
a=2
for i in range(3,100):
    for b in range(2,i):
        if i%b==0:
            break
    else:               #为什么else不和if缩进一样？
        a+=i
print(a)