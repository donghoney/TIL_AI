

def min_print(N):
    pow_point =0
    divisor_list=[]
    for i in range(1,pow(10,7)):
        if pow(i,2)<=N and pow(i+1,2)>N:
            pow_point=i
            break
    for i in range(0,pow_point):
        w=pow_point-i
        if N%w==0:
            h=N//w
            print('h : {} , w : {}'.format(h,w))
            return abs(h-w)






print(min_print(123))