try:
    x=float(input())    
    if x<=19:
        a=3.35*x
        b=2.4*x
        c=0.95*x
    elif x<=30:
        a=4.55*(x-19)+3.35*19
        b=3.6*(x-19)+2.4*19
        c=0.95*x    
    else:
        a=8.15*(x-30)+4.55*(30-19)+3.35*19
        b=7.2*(x-30)+3.6*(30-19)+2.4*19
        c=0.95*x        
    print("应缴水费：%.3f，其中：自来水费：%.3f，污水处理费：%.3f。"%(a,b,c))
except :
    print("输入错误！")