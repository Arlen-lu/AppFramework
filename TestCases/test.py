import os
import sys
sys.path.append(os.getcwd())
a = '剩余0天0时0分'
num = 0
for i in a:
    if i.isdigit() and int(i)>0:
        print(True)
        break
else:
    print(False)

money = '最大投资金额为:192039.0'
data = int(float(money.split(':')[1]))
print(data)
print(type(data))

a1 = '投资金额必须为100的整数倍'
a2 = '金额'
print(a2 in a1)

data = '最大投资金额为:192039.0元'
a =data.replace('元','').replace('最大投资金额为:','')
print(a)