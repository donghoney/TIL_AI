import numpy as np

def fv(cf,r,i):
    pv=cf*(1/pow((1+r),i))
    return pv

def pv(cf_0,r,n):
    pv=0
    for i in range(0,n+1):
        pv+=fv(cf_0,r,i)
    return pv

def main():
    cf_0 = 90
    r = 0.05
    print('PV of Constant Annuity (Equal Amount starts at 𝒕 = 𝟏 for 𝑵 periods)',str(cf_0/0.05))

    profitPresentValue=0
    netPresentValue=0
    front_t = 0

    dpp_mode = False
    irr_mode = True

    if dpp_mode:
        t_list = [i for i in range(0,50)]
        for i in t_list:
            if i>=3:
                profitPresentValue = pv(cf_0,r,i)-pv(cf_0,r,1)   #일정한 90만원의 연금 t=2 시점부터의 fv를 pv로 계산한 값들의 합 = 총 이익의 프로젝트 값
                netPresentValue = profitPresentValue - pv(200,0.05,3)+200 # 총이익의 합에서 t=1부터 t=3까지 3년간 200억의 투자금액 fv를 pv로 환산한 값들을 뺀 값
                netPresentValue -= 1000 # Net Present Value = Project Value
                print('t={} 까지의 NPV 는 {} 입니다.'.format(i,netPresentValue))
                if netPresentValue>0:
                    front_t=i-1
                    npv_t=netPresentValue
                    tplus=cf_0/pow((1+r),front_t+1)
                    dpp=front_t-(-npv_t*(1/tplus))
                    print('Discount Payback Period : {} '.format(dpp))

                    break
                else:
                    profitPresentValue = 0
                    netPresentValue = 0

    if irr_mode:
        eternity = 10000
        r_list = [i for i in np.arange(0.0,0.1,0.0001)]
        print(len(r_list))
        for i in r_list:
            profitPresentValue = pv(cf_0,i,eternity)-pv(cf_0,i,1)
            netPresentValue = profitPresentValue - pv(200, i,3) + 200  # 총이익의 합에서 t=1부터 t=3까지 3년간 200억의 투자금액 fv를 pv로 환산한 값들을 뺀 값
            netPresentValue -= 1000  # Net Present Value = Project Value
            #print(netPresentValue)
            print('r={} 일 때, NPV 는 {} 입니다.'.format(i, netPresentValue))
            if abs(netPresentValue)<0.1:
                print(netPresentValue,i)
                break


if __name__== '__main__':
    main()