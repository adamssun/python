#斐波那契数列计算
#获取用户输入整数N，其中，N为正整数
#计算斐波那契数列的值
#如果将斐波那契数列表示为fbi(N)，对于整数N，值如下：fbi(1)和fbi(2)的值是1，当N>2时，fbi(N) = fbi(N-1) + fbi(N-2)
def fbi(n):
    if n==1 or n==2:
        return 1
    else:
        return fbi(n-1)+fbi(n-2)
n=eval(input())
print(fbi(n))