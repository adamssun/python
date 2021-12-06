def cuml(a,*b):
    m=a
    for i in b:
        m*=i
    return m
print(eval('cuml({})'.format(input())))
9