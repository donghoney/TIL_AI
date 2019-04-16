import numpy as np

def pv(fv,r):
    pv=fv*(1/pow((1+r)))
    return pv

def npv(fv_list,r):
    npv=0
    for fv in fv_list:
        npv+=pv(fv,r)
    return npv

print('PV of Constant Annuity (Equal Amount starts at 𝒕 = 𝟏 for 𝑵 periods)',str(90/0.05))
print('NPV {}'.format(npv(90,0.05,10000)))

npv_profit =0

fv_90_list = [90 for i in range(0,1000)]

for fv in fv_90_list:
    total_profit_pv = npv(fv,0.05)-(90/(1+0.05))
    print(total_profit_pv)

if npv_profit>0:
    print(str(i)+'년째 부터 이익이 +입니다.')
    print('npv : {}'.format(npv_profit))
    break
else:
    total_profit=0
    npv_profit=0
