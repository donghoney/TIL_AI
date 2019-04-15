import numpy as np

def npv(fv,r,n):
    pv = 0
    for i in range(1,n):
        pv+=fv*(1/pow((1+r),i))
    return pv


npv_profit =0

num_list = [i for i in range(20,100)]

for i in num_list:
    total_profit_pv = npv(90,0.05,i)-(90/(1+0.05))
    #print(total_profit_pv)
    npv_profit = total_profit_pv- npv(200,0.05,3)
    #print(npv_profit)
    npv_profit -= 1000
    #print(npv_profit)
    if npv_profit>0:
        print(str(i)+'년째 부터 이익이 +입니다.')
        print('npv : {}'.format(npv_profit))
        break
    else:
        total_profit=0
        npv_profit=0
