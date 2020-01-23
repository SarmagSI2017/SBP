alpha = 0.8
w1=0
w2=0
thres=0.5
b=0.0
y_in=0
bias=1
x1=[1,1,0,0]
x2=[1,0,1,0]
t=[1,-1,-1,-1]
i=0
y=[0,0,0,0]
r=0
w1last=0
w2last=0
blast=0
btrans=[1.0]


while(True):
    print("----------------")
    print("epoh ke-",r+1)
    for i in range (4):
        print("----------------")
        print("data ke-",i+1)
        print(b,x1[i],w1,x2[i],w2)
        y_in=round(b+x1[i]*w1+x2[i]*w2,2)
        print("y_in=",y_in)
        if y_in >thres:
            y[i]=1
        elif y_in<thres*-1:
            y[i]=-1
        else:
            y[i]=0
        if y[i]!=t[i]:
            
            w1=round(w1+alpha*t[i]*x1[i],2)
            w2=round(w2+alpha*t[i]*x2[i],2)
            b=round(b+alpha*t[i],2)
            print("beda cuy")
        
        print("hasil aktivasi=",y[i])
        print("target=",t[i])
        print("w1=",w1)
        print("w2=",w2)
        print("b=",b)
    if(w1==w1last and w2==w2last and b==blast):
        break
    w1last=w1
    w2last=w2
    blast=b


    r+=1
print('\n\n')
print("pada epoh ke-",r+1," epoh dihentikan")
print("diperoleh nilai:")
print("w1 = ",w1)
print("w2 = ",w2)
print("bobot = ",b)




