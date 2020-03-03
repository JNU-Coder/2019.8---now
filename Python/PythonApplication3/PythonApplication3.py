import time
scale=50
print("zhi xing kai shi".center(scale//2,"-"))
start=time.perf_counter()
for i in range(scale+1):
    a='*'*i
    n='.'*(scale-i)
    c=(i/scale)*100
    dur=time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,n,dur),end='')
    time.sleep(0.1)
print("\nzhi xing jie shu".center(scale//2,"-"))