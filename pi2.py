#公式法
pi=0
N=10000
for k in range(0,N+1):
    pi=pi+1/pow(16,k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
print(pi)